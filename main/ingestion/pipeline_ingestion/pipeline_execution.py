import logging
import subprocess
import os
from datetime import datetime

# Lista de notebooks a ejecutar
notebooks = [
    r"C:\\Users\\dalarroy\\surf-prediction-project\\main\\bio\\bio_pysurfline.ipynb",
    r"C:\\Users\\dalarroy\\surf-prediction-project\\main\\bio\\bio_scrap.ipynb",
    r"C:\Users\\dalarroy\\surf-prediction-project\\main\\pg\\Ingesta_pysurfline.ipynb",
    r"C:\\Users\\dalarroy\\surf-prediction-project\\main\\pg\\surfline_scrap.ipynb",
    r"C:\\Users\\dalarroy\\surf-prediction-project\\main\\yatch\\yatch_pysurfline.ipynb",
    r"C:\\Users\\dalarroy\\surf-prediction-project\\main\\yatch\\yatch_scrap.ipynb",
]

# Directorio donde se guardarán los logs
log_dir = r"C:\\Users\\dalarroy\\surf-prediction-project\\logs"
os.makedirs(log_dir, exist_ok=True)  # Crear el directorio si no existe

# Configuración del logging
log_file = os.path.join(log_dir, "pipeline_execution.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()  # También imprime en la consola
    ],
)

# Ejecución de los notebooks
for notebook_path in notebooks:
    try:
        logging.info(f"Iniciando ejecución del notebook: {notebook_path}")
        subprocess.run(
            ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path],
            check=True,
            capture_output=True
        )
        logging.info(f"La ingesta del día {datetime.now()} para el notebook {notebook_path} fue exitosa")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error al ejecutar el notebook {notebook_path}: {e.stderr.decode('utf-8')}")
