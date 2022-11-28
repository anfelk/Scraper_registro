# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:30:53 2022

@author: ARIO
"""
# Importing the required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup


def func_emp(url, registro):
    # Downloading contents of the web page

    data = requests.get(url).text

    # Creating BeautifulSoup object
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find(
        'table', id='ctl00_ContentPlaceHolder1_gvFuncionEmpresas')

    # Defining of the dataframe
    ent_function = pd.DataFrame()

    # Collecting Ddata
    for row in table.find_all('tr'):
        # Find all data for each column
        columns = row.find_all('td')

        if (columns != []):
            funcion = columns[0].text.strip()
            if funcion == "Sin Funciones de Empresa":
                ent_function = ent_function.append(
                    {'Registro': registro, 'Función Empresa': "Sin Funciones de Empresa", 'Razón Social': "", 'País': ""}, ignore_index=True)
                exit
            else:
                razon = columns[1].text.strip()
                pais = columns[2].text.strip()
                ent_function = ent_function.append(
                    {'Registro': registro, 'Función Empresa': funcion, 'Razón Social': razon, 'País': pais}, ignore_index=True)

    return ent_function


def run():

    Funcion = func_emp(
        "https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP=H-1062/21", 'H-1062/21')

    Funcion.to_csv('outfile/funciontest.csv', encoding='utf-8', index=False)


if __name__ == '__main__':
    run()
