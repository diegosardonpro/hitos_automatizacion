import gspread
import os

# --- Settings ---
CREDENTIALS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'credentials', 'google_credentials.json'))
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']

# --- Google Sheets Client ---
class GoogleSheetsClient:
    """Un cliente que usa una ruta explícita al archivo de credenciales."""

    def __init__(self):
        print("Inicializando cliente de Google Sheets...")
        print(f"Leyendo credenciales desde: {CREDENTIALS_PATH}")
        self.client = gspread.service_account(filename=CREDENTIALS_PATH, scopes=SCOPES)
        print("Cliente de Google Sheets inicializado correctamente.")

    def add_scholarship(self, scholarship_data: dict, spreadsheet_id: str, worksheet_name: str):
        """
        Añade una beca a una hoja de cálculo específica usando su ID.
        """
        try:
            # Abre la hoja de cálculo por su ID, no por su nombre.
            spreadsheet = self.client.open_by_key(spreadsheet_id)
            print(f"Abriendo hoja de cálculo por ID: '{spreadsheet_id}'")

            try:
                worksheet = spreadsheet.worksheet(worksheet_name)
                print(f"Encontrada la hoja de trabajo: '{worksheet_name}'")
            except gspread.WorksheetNotFound:
                print(f"Hoja de trabajo '{worksheet_name}' no encontrada. Creándola...")
                worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows=100, cols=20)

            self._ensure_headers(worksheet, list(scholarship_data.keys()))

            new_row = list(scholarship_data.values())
            print(f"Añadiendo nueva fila: {new_row}")
            worksheet.append_row(new_row)
            print("Fila añadida exitosamente a Google Sheets.")
            return True

        except Exception as e:
            print(f"Error al interactuar con Google Sheets: {e}")
            print("Por favor, asegúrate de que el ID de la hoja es correcto y que fue compartida con el client_email.")
            return False

    def _ensure_headers(self, worksheet: gspread.Worksheet, headers: list):
        first_row = worksheet.row_values(1)
        if not first_row:
            print("La hoja está vacía. Escribiendo encabezados...")
            worksheet.update('A1', [headers])
            worksheet.format('A1:Z1', {'textFormat': {'bold': True}})
            print("Encabezados creados.")
        else:
            print("Encabezados ya presentes.")