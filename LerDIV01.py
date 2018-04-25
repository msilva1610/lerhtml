html_doc = '''
    <div class="block">
      <acn>1</acn> girar, rodar, virar(-se), volver(-se): <i data-toggle="tooltip" data-placement="top" data-original-title="he turned her head">he turned her head</i> / ele lhe virou a cabeça: <i data-toggle="tooltip" data-placement="top" data-original-title="it turns my stomach">it turns my stomach</i>      / está me virando o estômago: <i data-toggle="tooltip" data-placement="top" data-original-title="I don’t know which way to turn">I don’t know which way to turn</i> /
      <rn data-toggle="tooltip" data-placement="top" data-original-title="figurative(ly) / figurado">fig</rn> não sei o que fazer, não sei para que lado me virar: <i data-toggle="tooltip" data-placement="top" data-original-title="we turned the coat inside out">we turned the coat inside out</i> / viramos o paletó às avessas. </div>
    <div class="block">
      <acn>2</acn>
      <rn data-toggle="tooltip" data-placement="top" data-original-title="figurative(ly) / figurado">fig</rn> mudança de direção, reviravolta, crise, ação de virar. </div>
    <div class="block">
      <acn>3</acn> curva, cotovelo. </div>
    <div class="block">
      <acn>20</acn>
      <ra data-toggle="tooltip" data-placement="top" data-original-title="typography">Typogr</ra> letra bloqueada. </div>
'''
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
import pandas as pd

# conteudo = {'TipoCG':'', 'ACNID': '', 'ACNTexto':''}
global conteudo 

def main():
    # soup = BeautifulSoup(html_doc, "html.parser")
    # blocks = soup.find_all(class_="block")

    conteudo = {'TipoCG':'', 'ACNID': '', 'ACNTexto':''}

    with open("aim.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    verbete = soup.find(class_="verbete bs-component")

    blocks = verbete.find_all(class_="block")
    cg = ''
    acn = ''
    acntexto = ''
    for b in blocks:
        acn = ''
        for c in b.contents:
            if (isinstance(c, Tag)):
                if (c.name == 'cg'):
                    cg = c.get_text()
                    #print('conteudo tipocg: {}'.format(c.get_text()))
                elif (c.name == 'acn' and len(cg) > 0):
                    acn = c.get_text()
                    #print('conteudo acnid: {}'.format(c.get_text()))
            if (isinstance(c, NavigableString) and len(str(c).strip()) > 0):
                if (len(cg) > 0) and (len(acn) > 0) and len(acntexto) == 0:
                    acntexto = str(c)
                    print('CG:{},ACN:{}, acntexto:{} '.format(cg,acn,acntexto))
                    acn=''
                    acntexto=''
                elif len(acntexto) > 0:
                    break
if __name__ == "__main__":
    main()