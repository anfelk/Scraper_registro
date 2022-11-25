# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:54:36 2022

@author: ARIO
"""

from bs4 import BeautifulSoup
import requests
#import pandas as pd
#import re


def des_prod(url):

    #url = 'https://registrosanitario.ispch.gob.cl/'
    #url = 'https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP=F-25855/20'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Descripcion Producto
    det = soup.find_all('span')
    des_prod = []
    count = 0
    for i in det:
        if count < 15:
            des_prod.append(i.text)
        else:
            break
        count += 1

    return des_prod


def run():

    Descripcion = des_prod(
        "https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP=F-25855/20")
    print(Descripcion)


if __name__ == '__main__':
    run()
