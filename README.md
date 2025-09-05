
# Proyecto de Automatización de Becas

Este proyecto contiene una serie de automatizaciones para la recolección, procesamiento y gestión de información sobre becas, utilizando Airtable como base de datos central.

## Estructura del Proyecto

- `src/`: Código fuente principal.
  - `config/`: Módulos de configuración.
  - `data_extraction/`: Scripts para extraer datos de diversas fuentes.
  - `airtable_integration/`: Lógica para interactuar con la API de Airtable.
  - `utils/`: Funciones de utilidad (logging, limpieza de datos, etc.).
- `docs/`: Documentación del proyecto.
- `tests/`: Pruebas unitarias y de integración.
- `.env`: Archivo para variables de entorno (API keys, etc.). No versionado.
- `requirements.txt`: Dependencias de Python.

## Primeros Pasos

1. Renombrar `.env.example` a `.env`.
2. Rellenar las variables de entorno en `.env` con tus credenciales de Airtable.
3. Instalar las dependencias: `pip install -r requirements.txt`.
