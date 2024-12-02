# Importaciones
import pysurfline
import pandas as pd
from datetime import datetime
import os

# Definir el spotId para el cual quieres obtener las predicciones
spotId = "5842041f4e65fad6a7708ce3"

# Obtener la previsión de olas para los próximos 2 días con intervalos de 3 horas
spotforecasts = pysurfline.get_spot_forecasts(
    spotId,
    days=1,
    intervalHours=3,
)

# Convertir los resultados a un DataFrame
df_pysurfline = spotforecasts.get_dataframe()

# Filtrar las horas 6 am, 12 pm (Noon) y 6 pm
df_pysurfline = df_pysurfline[df_pysurfline['timestamp_dt'].dt.strftime('%H:%M').isin(['06:00', '12:00', '18:00'])]

# Ver las primeras filas del DataFrame
df_pysurfline.head()


# Definir la ruta de la carpeta 'data'
folder_path = "C:\\Users\\dalarroy\\surf-prediction-project\\data"

# Definir la ruta completa al archivo Excel
file_path = os.path.join(folder_path, "pg_pysurfline.xlsx")

# Crear la carpeta si no existe
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Verificar si el archivo ya existe
if os.path.exists(file_path):
    # Leer el archivo Excel existente
    existing_df = pd.read_excel(file_path, engine='openpyxl')
    
    # Concatenar el DataFrame existente con el nuevo DataFrame (df_pysurfline)
    df_combined = pd.concat([existing_df, df_pysurfline], ignore_index=True)
else:
    # Si el archivo no existe, usar solo el nuevo DataFrame
    df_combined = df_pysurfline

# Guardar el DataFrame combinado (nuevo + existente) en el archivo Excel
df_combined.to_excel(file_path, index=False, engine='openpyxl')

print(f"El DataFrame se ha guardado correctamente en '{file_path}'")