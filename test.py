# Knihovna pro stahování
import urllib.request
from tkinter import *
import wikipediaapi
from bs4 import BeautifulSoup
from urllib.request import urlopen
wiki = wikipediaapi.Wikipedia("cs")

wiki_page = wiki.page('Růže')
wiki_page_en = wiki_page.langlinks['en']
wiki_url = wiki_page_en.fullurl
print(wiki_url)
#wiki_url = 'https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)'
#html = urlopen(wiki_url)

#bs = BeautifulSoup(html, 'html.parser')
#print(wiki_url)
#img =  bs.find('img')
#print(img)
