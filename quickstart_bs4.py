# -*- coding: utf-8 -*-
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

# print(soup.title)

# print(soup.title.name)

# print(soup.title.string)

# print(soup.title.parent.name)

# print(soup.p)

# print(soup.p['class'])

# print(soup.a)

# print(soup.find_all('a'))

# print(soup.find(id='link3'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# Another common task is extracting all the text from a page:
# print(soup.get_text())

# soup1 = BeautifulSoup('<b class="boldest">Extremely bold</b>','html.parser')

# tag = soup1.b
# print(type(tag))
# print(tag.name)

# souptag = BeautifulSoup('<b id="boldest">','html.parser')
# b = souptag.find('b')
# print(souptag.find('b'))
# print(type(b))
# print(b['id'])
# print(b.attrs)

# Multi-valued attributes

# soup1 = BeautifulSoup('<b class="boldest">Extremely bold</b>','html.parser')

# css_soup = BeautifulSoup('<p class="body"></p>','html.parser')
# print(css_soup.p['class'])
# css_soup = BeautifulSoup('<p class="body strikeout"></p>','html.parser')
# print(css_soup.p['class'])

# id_soup = BeautifulSoup('<p id="my id"></p>','html.parser')
# print(id_soup.p['id'])
# print(id_soup)

# soup1 = BeautifulSoup('<b class="boldest">Extremely bold</b>','html.parser')
# tag = soup1.find('b')
# print(type(soup1))
# print(type(tag))
# print(tag.string)
# print(soup1.name)
# print(tag.name)

# print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

head_tag = soup.head
# print(head_tag)
# pegando o conteúdo de head, temos:
# print(head_tag.contents)

title_tag = head_tag.contents[0]
# print(title_tag)

# print(len(soup.contents))
# print(soup.contents[1].name)

# print(title_tag)
# print(type(title_tag))
# for child in title_tag.children:
#     print('child: {}'.format(child))

from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

def surrounded_by_strings1(tag):
    return (isinstance(tag.next_element, NavigableString))

tag = soup.find('b')
print(surrounded_by_strings1(tag))

for tag in soup.find_all(surrounded_by_strings1(tag)):
    print (tag.name)