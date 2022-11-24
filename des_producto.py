# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:54:36 2022

@author: ARIO
"""

from bs4 import BeautifulSoup
import requests
#import pandas as pd
#import re

#url = 'https://registrosanitario.ispch.gob.cl/'
url = 'https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP=F-25855/20'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


# Descripcion Producto

det = soup.find_all('span')

datos = []
count = 0
for i in det:
    if count < 15:
        datos.append(i.text)
    else:
        break
    count += 1


print(datos)
