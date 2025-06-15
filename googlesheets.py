# save data to google sheets
import gspread

ID_HOJA = "https://docs.google.com/spreadsheets/d/REEMPLAZAME/edit?usp=sharing"

def guardar_gsheets(data):
    # authenticate with google
    gc = gspread.service_account(filename='REEMPLAZAME.json')
    # open the sheet
    sheet = gc.open_by_url(ID_HOJA).sheet1
    # write the data to the sheet
    sheet.append_row(data)

mensaje = "De esta forma puedes enviar datos en vivo desde python a una hoja de Google Sheets"

guardar_gsheets(["test"])