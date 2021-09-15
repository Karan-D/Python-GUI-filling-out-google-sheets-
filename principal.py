
from tkinter import *
from gspread.utils import a1_to_rowcol
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient import discovery
from datetime import date
from ttkwidgets.autocomplete import AutocompleteCombobox



data = str(date.today())
cat = "categoria"
desc = "Descrição"
valor = "valor"

#print(data, desc)


def btclick():

    global data, cat, desc, valor
    #data = ed1.get()
    cat = ed2.get()
    desc = ed3.get()
    valor = ed4.get()
    janela.quit()



janela = Tk()



#entrada = Entry(janela)
#entrada.place(x=100, y=100)

lb1 = Label(janela, text="Forma de pagamento")
lb1.place(x=50, y=50)
cat_pagamento = ["Crédito", "Débito", "Dinheiro"]
ed1 = AutocompleteCombobox(janela, width=20, completevalues= sorted (cat_pagamento))
ed1.place(x=120, y=50)



lb2 = Label(janela, text="Categoria")
lb2.place(x=50,y=70)
cat_values = ["Alimentação", "Ferramentas manuais", "combustível", "Ferramentas elétricas"]     #Opções por categoria de custos
ed2 = AutocompleteCombobox(janela, width=20, completevalues = sorted(cat_values))
ed2.place(x=120, y=70)

lb3 = Label(janela, text="Descrição")
lb3.place(x=50,y=90)
ed3 = Entry(janela)
ed3.place(x=120, y=90)

lb4 = Label(janela, text="Valor R$")
lb4.place(x=50,y=110)
ed4 = Entry(janela)
ed4.place(x=120, y=110)

bt = Button(janela, width=20, text="Next", command=btclick)
bt.place(x=100, y=150)


janela.geometry("500x500+300+300")
janela.mainloop()
#print (data,desc)

#---------------------------------------------------------------------------------------------------------------------#

#ACCES SHEETS

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


atl = [[data,cat,desc,valor]]

request = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range="pag2!A:D", valueInputOption="USER_ENTERED", body={"values":atl}).execute()

print(request)