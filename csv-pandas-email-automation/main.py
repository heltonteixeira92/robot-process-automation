"""
This script takes some CSV files extracted from a sales software,
transforms them into a single Excel and sends by email
"""

import os
import pandas as pd

path = "bases"
files = os.listdir(path)

consolidated_table = pd.DataFrame()

for file in files:
    sales_table = pd.read_csv(os.path.join(path, file))
    sales_table['Data de Venda'] = pd.to_datetime("01/01/1900") + pd.to_timedelta(sales_table['Data de Venda'],
                                                                                  unit="d")
    consolidated_table = pd.concat([consolidated_table, sales_table])

consolidated_table = consolidated_table.sort_values(by="Data de Venda")

consolidated_table = consolidated_table.reset_index(drop=True)

consolidated_table.to_excel("Vendas.xlsx", index=False)
