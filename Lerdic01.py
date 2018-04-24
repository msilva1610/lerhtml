html_doc = """
    <div class="block">
      <acn>1</acn> rotação, volta, giro: <i data-toggle="tooltip" data-placement="top" data-original-title="I took two turns up and down the room">I took two turns up and down the room</i> / andei duas vezes para cá e para lá dentro do quarto. </div>
"""
from bs4 import NavigableString
import pandas as pd
from bs4 import BeautifulSoup

soup_local = BeautifulSoup(html_doc, "html.parser")
div_texto = str(soup_local.get_text())
# print(div_texto)
texto_acn = str(soup_local.find("acn").get_text())
print(texto_acn)
novodivtexto = div_texto.replace(texto_acn,"")
print(novodivtexto.strip())
# encontra o dois pointos (:)
doispontos = novodivtexto.find(":")
print(novodivtexto[:doispontos].strip())