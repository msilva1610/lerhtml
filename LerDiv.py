html_doc = '''
    <div class="block">
      <acn>1</acn> girar, rodar, virar(-se), volver(-se): <i data-toggle="tooltip" data-placement="top" data-original-title="he turned her head">he turned her head</i> / ele lhe virou a cabeça: <i data-toggle="tooltip" data-placement="top" data-original-title="it turns my stomach">it turns my stomach</i>      / está me virando o estômago: <i data-toggle="tooltip" data-placement="top" data-original-title="I don’t know which way to turn">I don’t know which way to turn</i> /
      <rn data-toggle="tooltip" data-placement="top" data-original-title="figurative(ly) / figurado">fig</rn> não sei o que fazer, não sei para que lado me virar: <i data-toggle="tooltip" data-placement="top" data-original-title="we turned the coat inside out">we turned the coat inside out</i> / viramos o paletó às avessas. </div>
'''
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
import pandas as pd


soup = BeautifulSoup(html_doc, "html.parser")
# print(soup.prettify())
# print(soup)
# print(type(soup))

tag = soup.find(class_="block")
# del tag['i']

# print(tag.contents)

conteudo = {'ACNID': '', 'ACNTEXTO':''}
print(conteudo)

for content in tag.contents:
    if (isinstance(content, Tag)):
        #print(type(content))
        #print(content)
        print('content name: {}'.format(content.name))
        if (content.name == 'acn'):
            # print('acn next text: {}'.format(content.next_element))
            conteudo['ACNID'] = str(content.get_text())
            # print(conteudo)
            # break
    if (isinstance(content, NavigableString)):
        if (len(conteudo['ACNID']) > 0 and len(conteudo['ACNTEXTO']) == 0 ):
             conteudo['ACNTEXTO'] = str(content)
             print(conteudo)
        #print(type(content))
        # print(content)
        # print('content name: {}'.format(content.name))
    #print ('==========================================================')
# i=tag.find_all('i')
# print (i.attrs)
# print(len(i))
# for item in i:
#     print(item)
# #print (tag.get_text())