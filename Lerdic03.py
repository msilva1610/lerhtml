# -*- coding: utf-8 -*-
from bs4 import NavigableString
import pandas as pd
from bs4 import BeautifulSoup
import types 

with open("MICHAELIS.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

verbete = soup.find(class_="verbete bs-component")

block = verbete.find_all(class_="block")

arrCG = []
arrTextoACN = []
tipo = ""
linha = ""
LinhaSemAcn = ""

for linha in block:
    if (linha.find("cg")):
        tipo = linha.find("cg").get_text()
    if (linha.find('sx')):
        break
    elif (linha.find("acn")):
        TextoLinha = linha.get_text()
        TextoACN = linha.find('acn').get_text()
        LinhaSemAcn = TextoLinha.replace(TextoACN,"").strip() 
        DoisPontos = LinhaSemAcn.find(":")
        if (LinhaSemAcn.find(":") > 0):
            LinhaSemAcn = LinhaSemAcn[:DoisPontos]
        arrCG.append(tipo)  
        arrTextoACN.append(LinhaSemAcn)

dfarrCG = pd.DataFrame({
    "tipo":arrCG,
    "TextoACN": arrTextoACN
})
# t = dfarrCG['TextoACN'][5] 
# print(t)
print(dfarrCG)

