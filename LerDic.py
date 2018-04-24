html_doc = """
    <div class="block">
      <acn>1</acn> rotação, volta, giro: <i data-toggle="tooltip" data-placement="top" data-original-title="I took two turns up and down the room">I took two turns up and down the room</i> / andei duas vezes para cá e para lá dentro do quarto. </div>
"""
from bs4 import NavigableString
import pandas as pd
from bs4 import BeautifulSoup
import types 

with open("MICHAELIS.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")



# print(soup)

# ler
# <div class="verbete bs-component">
verbete = soup.find(class_="verbete bs-component")
# print (verbete)
# print(len(verbete))

block = verbete.find_all(class_="block")
# block = verbete.find(class_="block")
# print (block)
# print(verbete['class'])
# ['verbete', 'bs-component']

e1 = verbete.select("div e1")
cg = verbete.select("div cg")
es = verbete.select("div es")
acn_tags = verbete.select("div acn")
i = verbete.select("div i")

acn_text = verbete.select("div acn")
acn_find = verbete.find_all("acn")
print (type(verbete))

print(len(verbete))

# i = 0;
# for item in verbete:
#     if isinstance(item, NavigableString):
#         continue
#     else:
#         print (item.name)
#         print (item.get_text())

soup_local = BeautifulSoup(html_doc, "html.parser")
div_texto = soup_local.get_text()
print(div_texto)
texto_acn = soup_local.find("acn")
texto_sem_acn = div_texto.replace(str(texto_acn),"")
print(texto_sem_acn)

# print (texto_acn.get_text())

# print(soup_local.get_text())

# for item in soup_local:
#     print("linha...")
#     print (item)
# deu certo
#print(soup_local.find('i').get_text())

    # else:
    #     print (type(item))

# print(verbete.find(class_="block"))
# print(verbete.select("acn"))

# print (i)
# e1 = block.select("div e1")
# print(e1)
# print (cg)
# print (es)
# print (acn_tags)

acn_itens = [acn.get_text() for acn in acn_tags]
# print(acn_itens)

tabdic = pd.DataFrame({
    "acn": acn_itens
})
# print(tabdic)