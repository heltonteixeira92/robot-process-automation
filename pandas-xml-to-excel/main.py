import xmltodict
import os
import pandas as pd
import json


def get_infos(file, valores):
    with open(f'nfs/{file}', "rb") as file_xml:
        file_dict = xmltodict.parse(file_xml)
        # print(json.dumps(file_dict, indent=4))

        if 'NFe' in file_dict:
            nf_infos = file_dict['NFe']['infNFe']
        else:
            nf_infos = file_dict['nfeProc']['NFe']['infNFe']

        numero_nota = nf_infos['@Id']
        empresa_emissora = nf_infos['emit']['xNome']
        nome_cliente = nf_infos['dest']['xNome']
        endereco = nf_infos['dest']['enderDest']
        if 'vol' in nf_infos['transp']:
            peso = nf_infos['transp']['vol']['pesoB']
        else:
            peso = "Não informado"

        valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso])


files = os.listdir('nfs')

colunas = ['numero_nota', 'empresa_emissora', 'nome_cliente', 'endereco', 'peso']
valores = []
for file in files:
    get_infos(file, valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFicais.xlsx", index=False)
