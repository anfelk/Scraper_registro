import pandas as pd
import get_list
import des_prod
import func_empresa


URL_root = "https://registrosanitario.ispch.gob.cl/Ficha.aspx?RegistroISP="
Directa = 'src/ProductosDirecta.csv'
RecetaCheque = 'src/ProductosRecetaCheque.csv'
RecetaMedica = 'src/ProductosRecetaMedica.csv'


def cond_venta(tipo_venta):
    if tipo_venta == "Directa":
        archivo = Directa
    elif tipo_venta == "RecetaCheque":
        archivo = RecetaCheque
    elif tipo_venta == "RecetaMedica":
        archivo = RecetaMedica
    else:
        print('Opcion invalida')
        exit
    return archivo


tipo_venta = input('ingrese condicion de venta => ')
archivo = cond_venta(tipo_venta)

# Cabecera registros descripcion
Cabecera = ("'Registro' , 'Nombre', 'Referencia de Tramite', 'Equivalencia Terapéutica o Biosimilar', 'Titular', 'Estado del Registro', 'Resolución Inscríbase', 'Fecha Inscríbase', 'Ultima Renovación', 'Fecha Próxima renovación, Régimen', 'Vía Administración', 'Condición de Venta', 'Expende tipo establecimiento', 'Indicación'")
with open(f'outfile/descripcion_{tipo_venta}.csv', 'a+', encoding='utf-8') as f:
    f.write(Cabecera)
    f.write('\n')

funcion = pd.DataFrame()
funcion_final = pd.DataFrame()
list_links = get_list.get_links(archivo)
for link in list_links:
    URL = URL_root + link
    descripcion = des_prod.des_prod(URL)
    descripcion = str(descripcion)
    descripcion = descripcion.replace('[', '')
    descripcion = descripcion.replace(']', '')
    with open(f'outfile/descripcion_{tipo_venta}.csv', 'a+', encoding='utf-8') as f:
        f.write(descripcion)
        f.write('\n')
    if len(funcion.columns) == 0:
        funcion = func_empresa.func_emp(URL, link)
    else:
        funcion_temp = func_empresa.func_emp(URL, link)
        funcion_final = funcion.merge(funcion_temp, how='outer')
        funcion = funcion_final
    funcion_final.to_csv(
        f'outfile/funcion_{tipo_venta}.csv', encoding='utf-8', index=False)
