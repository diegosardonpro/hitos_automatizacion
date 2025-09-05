import os
from dotenv import load_dotenv

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path=dotenv_path, override=True)

print(f"Cargando .env desde: {dotenv_path}")

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")


if not all([AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME]):
    raise ValueError("Error: Una o mas variables de entorno de Airtable no estan definidas. Revisa tu archivo .env.")



LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


print("Configuracion cargada correctamente.")
print(f"Airtable Base ID: {AIRTABLE_BASE_ID}")
print(f"Airtable Table Name: {AIRTABLE_TABLE_NAME}")