import pandas as pd
import get_list
import des_prod
import func_empresa

URL_root = "https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP="

list_links = get_list.get_links()

for link in list_links:
    URL = URL_root + link
    descripcion = des_prod.des_prod(URL)
    funcion = func_empresa.func_emp(URL, link)
    print(funcion)
