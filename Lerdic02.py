# -*- coding: utf-8 -*-
from bs4 import NavigableString
import pandas as pd
from bs4 import BeautifulSoup
import types 

with open("MICHAELIS.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

verbete = soup.find(class_="verbete bs-component")

# short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

block = verbete.find_all(class_="block")
# arrBlock = [item for item in block]
# print(arrBlock)

# divEmLinha = pd.DataFrame({
#     "coluna1": arrBlock
# })
# print(divEmLinha)

arrCG = []
arrTextoACN = []
tipo = ""
for linha in block:
    if (linha.find("cg")):
        tipo = linha.find("cg").get_text()
    if (linha.find('sx')):
        break
    else:
        arrCG.append(tipo)  
        arrTextoACN.append(linha.get_text())      
# print(arrCG)
print(block[62])
dfarrCG = pd.DataFrame({
    "tipo":arrCG,
    "TextoACN": arrTextoACN
})
t = dfarrCG['TextoACN'][5]
print(t)
# print(dfarrCG['TextoACN'])

#proximos passos:
# validar se o dataframe esta carregando as colunas corretas
# usar o python ide para resolver o problema do utf-8