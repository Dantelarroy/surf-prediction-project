from datetime import datetime
import time
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import pandas as pd

# Configurar Selenium con el controlador del navegador
driver = webdriver.Chrome()  # Asegúrate de tener el controlador instalado y configurado
url = "https://www.surfline.com/surf-report/playa-grande/5842041f4e65fad6a7708ce3?view=table"
driver.get(url)

# Esperar a que la página cargue completamente
time.sleep(5)  # Ajusta el tiempo según la velocidad del sitio

# Obtener el HTML generado
html = driver.page_source

# Analizar con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extraer tablas relevantes (Tabla 2, Tabla 3, Tabla 4)
tables = soup.find_all('table')

# Procesar tabla 2 (Horas del día)
table_2 = tables[1]
rows_table_2 = table_2.find_all('tr')
times = [row.find_all('td')[0].get_text(strip=True) for row in rows_table_2]

# Procesar tabla 3 (Información de olas y viento)
table_3 = tables[2]
rows_table_3 = table_3.find_all('tr')
data_table_3 = []
for row in rows_table_3:
    cells = row.find_all('td')
    data_row = [cell.get_text(strip=True) for cell in cells]
    
    # Corregir formato para las columnas de Swell y Wind
    for idx in [2, 3, 4]:  # Índices de Primary Swell, Secondary Swell 1, Secondary Swell 2
        if idx < len(data_row):
            data_row[idx] = data_row[idx].replace("m", "m ").replace("s", "s")
    data_row[5] = data_row[5].replace("kph", " kph")  # Corregir formato del viento
    
    data_table_3.append(data_row)

# Procesar tabla 4 (Información meteorológica)
table_4 = tables[3]
rows_table_4 = table_4.find_all('tr')
data_table_4 = []
for row in rows_table_4:
    cells = row.find_all('td')
    data_table_4.append([cell.get_text(strip=True) for cell in cells])
    
print(f'{times}\n{"*"*50}\n{data_table_3}\n{"*"*50}\n{data_table_4}')


# Definir la fecha de hoy
today_date = datetime.today().strftime('%Y-%m-%d')

# Asegúrate de que todas las listas tengan la misma longitud (tomando la longitud mínima)
min_length = min(len(times), len(data_table_3), len(data_table_4))

# Recortar las listas
times = times[:min_length]
data_table_3 = data_table_3[:min_length]
data_table_4 = data_table_4[:min_length]

# Combinar los datos en un DataFrame
combined_data = []
for i in range(min_length):
    combined_data.append({
        "Date": today_date,  # Agregar columna de fecha
        "Time": times[i],
        "Surf(m)": data_table_3[i][0],  # Primera columna de la tabla 3
        "Rating": data_table_3[i][1],  # Segunda columna de la tabla 3
        "Primary Swell": data_table_3[i][2],  # Tercera columna de la tabla 3
        "Secondary Swell": f"{data_table_3[i][3]} | {data_table_3[i][4]}",  # Combina Swell 2 y Swell 3
        "Wind": data_table_3[i][5],  # Sexta columna de la tabla 3
        "Temperature": data_table_4[i][0],  # Primera columna de la tabla 4
        "Pressure": data_table_4[i][1],  # Segunda columna de la tabla 4
        "Probability": data_table_4[i][2],  # Tercera columna de la tabla 4
    })

df_scrap = pd.DataFrame(combined_data)

# Definir la ruta completa al archivo Excel
file_path = "C:\\Users\\dalarroy\\surf-prediction-project\\data\\pg_scrap_surfline.xlsx"

# Leer el archivo Excel si existe
if os.path.exists(file_path):
    # Cargar los datos existentes
    existing_df = pd.read_excel(file_path, engine='openpyxl')
    
    # Eliminar las filas duplicadas basándose solo en la columna "Date" para evitar añadir las mismas filas
    df_scrap = pd.concat([existing_df, df_scrap]).drop_duplicates(subset=["Date"], keep="last").reset_index(drop=True)
else:
    # Si el archivo no existe, solo usa los datos nuevos
    df_scrap = df_scrap.reset_index(drop=True)

# Guardar el DataFrame actualizado en el archivo Excel
df_scrap.to_excel(file_path, index=False, engine='openpyxl')

print(f"El DataFrame se ha guardado correctamente en '{file_path}'")

