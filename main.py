import pandas as pd
import get_list
import des_prod
import func_empresa

URL_root = "https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP="

list_links = get_list.get_links()

for link in list_links:
    URL = URL_root + link
    descripcion = des_prod.des_prod(URL)
    descripcion = str(descripcion)
    with open('outfile/descripcion.csv', 'w', encoding='utf-8') as f:
        f.write(descripcion)

    funcion = func_empresa.func_emp(URL, link)
    funcion = str(funcion)
    with open('outfile/funcion.csv', 'w', encoding='utf-8') as f:
        f.write(funcion)
