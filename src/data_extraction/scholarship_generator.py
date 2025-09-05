import json

def get_scholarship_prompt() -> str:
    """
    Retorna el prompt estructurado para solicitar la generación de datos de una beca en formato JSON.
    """
    prompt = (
        "Actúa como un asistente de creación de oportunidades educativas. "
        "Genera los detalles para una beca ficticia pero realista. "
        "Quiero la respuesta únicamente en formato JSON, sin texto introductorio ni explicaciones. "
        "La estructura debe ser: "
        "{\"nombre\": \"...\", \"descripcion\": \"...\", \"monto\": ..., \"area\": \"...\", \"fecha_limite\": \"YYYY-MM-DD\"}. "
        "Para el campo 'area', elige una de estas opciones exactamente: "
        "Salud, Ingeniería, Educación, Ciencias Sociales, Tecnología, Artes. "
        "El monto debe ser un número entero, sin símbolos de moneda."
    )
    return prompt

def parse_scholarship_json(json_string: str) -> dict | None:
    """
    Intenta parsear una cadena de texto JSON a un diccionario de Python.
    Realiza una validación para asegurar que es un JSON válido y contiene las claves esperadas.

    Args:
        json_string (str): La respuesta en formato de texto del LLM.

    Returns:
        dict | None: Un diccionario con los datos de la beca si el parseo es exitoso, de lo contrario None.
    """
    try:
        # Limpieza preliminar para eliminar bloques de código markdown que los LLMs a veces añaden.
        if '```json' in json_string:
            clean_json_string = json_string.split('```json')[1].split('```')[0].strip()
        else:
            # Si no hay bloque de código, busca el JSON entre llaves
            start = json_string.find('{')
            end = json_string.rfind('}') + 1
            if start == -1 or end == 0:
                raise json.JSONDecodeError("No se encontraron llaves de JSON", json_string, 0)
            clean_json_string = json_string[start:end]

        data = json.loads(clean_json_string)

        # Validación de claves y tipos básicos
        expected_keys = {"nombre": str, "descripcion": str, "monto": int, "area": str, "fecha_limite": str}
        for key, expected_type in expected_keys.items():
            if key not in data:
                print(f"❌ Error de parseo: La clave '{key}' falta en el JSON generado.")
                return None
            if not isinstance(data[key], expected_type):
                print(f"Error de parseo: La clave '{key}' tiene un tipo incorrecto. Se esperaba {expected_type.__name__}.")
                return None

        print("JSON de beca parseado y validado correctamente.")
        return data
    except json.JSONDecodeError:
        print(f"❌ Error de parseo: La respuesta del modelo no es un JSON válido.")
        print(f"Respuesta recibida:\n---\n{json_string}\n---")
        return None
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado durante el parseo: {e}")
        return None