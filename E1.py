from pyhunter import PyHunter
from openpyxl import Workbook
import getpass
import re


def busqueda(organizacion):
    # Cantidad de resultados esperados de la búsqueda
    # El límite MENSUAL de Hunter es 50, cuidado!
    resultado = hunter.domain_search(
        company=organizacion,
        limit=1,
        emails_type='personal'
    )
    return resultado


def guardar_informacion(datosEncontrados, organizacion):
    libro = Workbook()
    hoja = libro.create_sheet(organizacion)
    libro.save("Hunter" + organizacion + ".xlsx")
    lista_correos = []
    aux = str(datosEncontrados)
    correos = re.findall(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}", aux)
    lista_correos.append(str(correos))
    hoja.append(lista_correos)
    libro.save("Hunter" + organizacion + ".xlsx")


print("Script para buscar información")
apikey = getpass.getpass("Ingresa tu API key: ")
hunter = PyHunter(apikey)
orga = input("Dominio a investigar: ")
datosEncontrados = busqueda(orga)
if datosEncontrados is None:
    exit()
else:
    print(datosEncontrados)
    print(type(datosEncontrados))
    guardar_informacion(datosEncontrados, orga)
