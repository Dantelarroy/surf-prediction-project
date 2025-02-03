Fases del Proyecto

1. Estructuración y Planificación

Definir objetivos y alcance del proyecto.

Identificar los datasets necesarios (variables climáticas y oceánicas de 3 puntos dentro de una playa, de 2 fuentes distintas).

Elegir las herramientas y tecnologías a utilizar (PyTorch/TensorFlow, pandas, Ollama, LangChain).

Estructurar el proyecto en VSCode y GitHub, incluyendo:

Carpeta data/: Contiene los datasets crudos y procesados.

Carpeta logs/: Guarda los registros de ejecución del modelo.

Carpeta main/: Incluye subcarpetas para cada playa y notebooks del scraping realizado.

Archivos de configuración y documentación.

2. Procesamiento y Limpieza de Datos

Carga de datos: Unificar las 6 fuentes de datos en un solo DataFrame.

Preprocesamiento:

Normalización y conversión de unidades.

Tratamiento de valores nulos y outliers.

Interpolación de datos faltantes.

Conversión de fechas y horas a un formato uniforme.

Generación de features adicionales.

Resultado esperado: DataFrame listo para entrenar modelos.

3. Creación del Sistema de Puntaje para Condiciones de Surf

Definir una métrica de rating de surf, considerando:

Altura de olas

Dirección del viento

Período de olas

Marea

Generar una puntuación global basada en condiciones ideales para surfistas.

4. Entrenamiento de Modelos de Deep Learning

Modelos a probar:

LSTM / GRU: Para datos secuenciales.

CNN 1D: Para detección de patrones en series temporales.

Transformers para Time Series.

Evaluación de modelos:

Comparar métricas (MSE, RMSE, precisión, recall).

Validación cruzada y ajuste de hiperparámetros.

5. Creación de un Extractor de Datos en Tiempo Real

Desarrollar un scraper o utilizar APIs para obtener condiciones climáticas de todas las playas disponibles.

Guardar la información en una base de datos para el modelo de predicción.

6. Aplicación del Modelo de Predicción

Ejecutar el modelo entrenado en las nuevas condiciones climáticas diarias.

Predecir el mejor spot dentro de la playa.

7. Integración de un LLM para Recomendaciones de Playas

Implementar un LLM que analice los resultados del modelo y compare múltiples playas cercanas.

Diseñar prompts dinámicos para generar recomendaciones personalizadas.

Integrar un chatbot que responda en lenguaje natural sobre la mejor playa para surfear cada día.

Tecnologías Utilizadas

Procesamiento de Datos: Pandas, NumPy

Modelado: TensorFlow / PyTorch

Scraping / APIs: BeautifulSoup, requests

LLM: Ollama + LangChain + Llama3 / GPT-4o

Backend / UI: FastAPI / Streamlit / WhatsApp Bot

Próximos Pasos

Estructurar el proyecto en GitHub y VSCode.

Limpieza de datos y creación del DataFrame final.

Implementación del sistema de puntaje para surf.

Entrenamiento del modelo de predicción.

Creación del scraper para obtener datos en tiempo real.

Aplicación del modelo en condiciones actuales.

Desarrollo del chatbot con LLM.

