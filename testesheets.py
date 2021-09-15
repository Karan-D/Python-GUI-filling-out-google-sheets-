from gspread.utils import a1_to_rowcol
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient import discovery

#from tkinter import *


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)

#the ID Spreadsheet.
SPREADSHEET_ID = '1jFsgA0UPdZrrlbQO1uxgcqIaS8OzMAKhD1ln0yz71Z0'

service = build('sheets', 'v4' ,credentials=creds)



# call the sheets API

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="pag2!A1:D40").execute()

values = result.get('values',[])


# INTERFACE GRÁFICA


data = input('Qual a data?')
desc = input('Descrição:')
cat = input ("Digite a categoria:")
#fdp = input ('Forma de pagamento:')
#valor = input('Digite o valor:')

atl = [[data,desc,cat]]

request = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range="pag2!A1", valueInputOption="USER_ENTERED", body={"values":atl}).execute()

print(request)