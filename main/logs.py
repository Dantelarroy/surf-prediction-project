import logging
from datetime import datetime

# Configuración del logger
log_filename = "data/surf_data_scraper.log"  # Ubicación del archivo de log
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,  # Puedes usar DEBUG para más detalle
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def log_success():
    """Registra un mensaje de éxito"""
    logging.info("Daily Surf Data Scraper completed successfully. XLSX files have been updated.")

def log_error(error_message):
    """Registra un mensaje de error"""
    logging.error(f"Error occurred: {error_message}")

if __name__ == "__main__":
    # Aquí iría la lógica principal de ejecución del scraper
    try:
        # Simula la ejecución de tus scripts
        # Por ejemplo: ejecutar los notebooks o tus scripts principales.
        
        # Si todo va bien, se registra como éxito
        log_success()
    except Exception as e:
        # Si ocurre un error, se captura la excepción y se registra el error
        log_error(str(e))
