
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# --- Carga de Configuración ---
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'hitos_automatizacion', '.env'))
load_dotenv(dotenv_path=dotenv_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("No se encontró la GEMINI_API_KEY en el archivo .env del proyecto de hitos")

genai.configure(api_key=GEMINI_API_KEY)

def get_milestone_extraction_prompt():
    """
    Retorna el prompt específico para extraer datos de un archivo de documentación de hito.
    """
    prompt = (
        '''Actúa como un asistente de gestión de proyectos. Analiza el siguiente texto, que es la documentación de un hito de proyecto, y extrae la información solicitada. Quiero la respuesta únicamente en formato JSON, sin texto introductorio, explicaciones ni saltos de línea. La estructura del JSON debe ser la siguiente: {"ID Hito": "...", "Nombre del Hito": "...", "Fecha": "YYYY-MM-DD", "Estado": "...", "Objetivos Cumplidos": "...", "Entregables": "...", "Valor Aportado": "...", "Horas Estimadas (sin IA)": ...}. Para el campo 'Horas Estimadas (sin IA)', extrae solo el valor numérico. Resume los objetivos, entregables y valor en texto claro.'''
    )
    return prompt

def extract_milestone_data(text_content: str) -> dict | None:
    """
    Usa el modelo Gemini para extraer datos estructurados de un texto de hito.
    """
    primary_model = 'gemini-1.5-pro'
    fallback_model = 'gemini-1.5-flash'
    
    prompt = get_milestone_extraction_prompt()
    full_prompt = prompt + '\n\n--INICIO DEL DOCUMENTO--\n' + text_content + '\n--FIN DEL DOCUMENTO--'

    try:
        print(f"Contactando a la API de Gemini con el modelo prioritario: {primary_model}...")
        model = genai.GenerativeModel(primary_model)
        response = model.generate_content(full_prompt)
    except Exception as e:
        print(f"El modelo '{primary_model}' falló. Error: {e}")
        print(f"Reintentando automáticamente con el modelo de respaldo: {fallback_model}...")
        try:
            model = genai.GenerativeModel(fallback_model)
            response = model.generate_content(full_prompt)
        except Exception as final_e:
            print(f"El modelo de respaldo también falló. Error: {final_e}")
            return None

    try:
        json_response_text = response.text.strip().replace("\n", "").replace("```json", "").replace("```", "")
        print("Respuesta de la IA recibida. Parseando JSON...")
        data = json.loads(json_response_text)
        print("JSON de Hito parseado con éxito.")
        return data
    except Exception as e:
        print(f"Error al parsear la respuesta de la IA: {e}")
        print(f"Respuesta recibida del modelo: {response.text}")
        return None
