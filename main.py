import pandas as pd
import get_list
import des_prod
import func_empresa


# def write_file(data):


URL_root = "https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP="
#archivo = 'src/ProductosDirecta.csv'
archivo = 'src/ProductosRecetaMedica.csv'

list_links = get_list.get_links(archivo)

for link in list_links:
    URL = URL_root + link
    descripcion = des_prod.des_prod(URL)
    descripcion = str(descripcion)
    descripcion = descripcion.replace('[', '')
    descripcion = descripcion.replace(']', '')
    with open('outfile/descripcion.csv', 'a+', encoding='utf-8') as f:
        f.write(descripcion)
        f.write('\n')

    #funcion = func_empresa.func_emp(URL, link)
    #funcion = str(funcion)
    # with open('outfile/funcion.csv', 'a+', encoding='utf-8') as f:
    #    f.write(funcion)
