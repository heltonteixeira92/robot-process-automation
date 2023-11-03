"""https://pypi.org/project/pywin32/ only works on windows"""

import os
import win32com.client as win32
from datetime import datetime

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)
email.To = "meuemail@gmail.com"
today = datetime.today().strftime('%d/%m/%Y')
email.Subject = f"Relation de Vendas {today}"
email.Body = f"""
Prezados,

Segue em anexo o Relatório de Vendas de {today} atualizado.
Att
"""

path = os.getcwd()
anexo = os.path.join(path, "Vendas.xlsx")
email.Attachments.Add(anexo)

email.Send()
