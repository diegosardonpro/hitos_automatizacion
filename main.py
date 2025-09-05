import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from src.google_sheets_client import GoogleSheetsClient
from src.ai_processor import extract_milestone_data

# --- Configuración ---
INPUT_DIR = os.path.join(os.path.dirname(__file__), 'input_documents')
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), 'processed_documents')
# ID de la hoja de cálculo para los Hitos
SPREADSHEET_ID = "1HJgox5vyBsQE1lqnHjMRNKApmF_rXscWX3lgX0iJUZw"
WORKSHEET_NAME = "Registro de Hitos"

def read_file_content(file_path: str) -> str | None:
    """Lee todo el texto de un archivo .md."""
    try:
        print(f"Leyendo archivo: {os.path.basename(file_path)}")
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        print("Lectura de archivo completada.")
        return text
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def process_single_file(file_name: str, sheets_client: GoogleSheetsClient):
    """Procesa un único archivo de hito."""
    file_path = os.path.join(INPUT_DIR, file_name)
    
    print(f"--- Procesando archivo: {file_name} ---")
    text_content = read_file_content(file_path)
    if not text_content:
        return

    milestone_data = extract_milestone_data(text_content)
    if not milestone_data:
        print(f"La extracción con IA falló para {file_name}. Omitiendo.")
        return

    success = sheets_client.add_scholarship(milestone_data, SPREADSHEET_ID, WORKSHEET_NAME)

    if success:
        time.sleep(1)  # Pausa para liberar el archivo
        destination_path = os.path.join(PROCESSED_DIR, file_name)
        try:
            os.rename(file_path, destination_path)
            print(f"Archivo movido a: {destination_path}")
            print(f"--- Procesamiento de {file_name} completado con éxito. ---")
        except Exception as e:
            print(f"Error al mover el archivo {file_name}: {e}")
    else:
        print(f"--- Falló el procesamiento de {file_name}. El archivo no fue movido. ---")

def main():
    """
    Orquesta el flujo de trabajo para procesar todos los archivos de hitos pendientes.
    """
    print("--- Iniciando Sistema de Automatización de Hitos ---")
    sheets_client = GoogleSheetsClient() # Inicializar el cliente una sola vez

    print(f"Buscando archivos de Hitos (.md) en: {INPUT_DIR}")
    try:
        files_to_process = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.md')]

        if not files_to_process:
            print("No se encontraron archivos para procesar.")
        else:
            print(f"Se encontraron {len(files_to_process)} archivo(s) para procesar.")
            for file_name in files_to_process:
                process_single_file(file_name, sheets_client)
                time.sleep(2) # Pequeña pausa entre archivos

    except Exception as e:
        print(f"Ocurrió un error en el ciclo principal: {e}")
    
    print("\n--- Proceso de Hitos finalizado. ---")

if __name__ == "__main__":
    main()
