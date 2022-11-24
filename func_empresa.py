# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:30:53 2022

@author: ARIO
"""

# Importing the required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Downloading contents of the web page
url = "https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP=F-25855/20"
#url = "https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP=F-21166/19"
data = requests.get(url).text

# Creating BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')


#tables = soup.find_all('table')
table = soup.find('table', id='ctl00_ContentPlaceHolder1_gvFuncionEmpresas')

# Defining of the dataframe
emp_function = pd.DataFrame(
    columns=['Función Empresa', 'Razón Social', 'País'])

# Collecting Ddata
for row in table.find_all('tr'):
    # Find all data for each column
    columns = row.find_all('td')

    if (columns != []):
        funcion = columns[0].text.strip()
        razon = columns[1].text.strip()
        pais = columns[2].text.strip()

        emp_function = emp_function.append(
            {'Función Empresa': funcion,  'Razón Social': razon, 'País': pais}, ignore_index=True)
