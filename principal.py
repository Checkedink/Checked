try:
    from googlesearch import search
    from bs4 import BeautifulSoup
    import ssl
    from urllib.request import urlopen
    import pandas as pd
    import numpy as np
except ImportError:
    print("One module is missing found")
# Que se va a buscar

# Los links resultantes de la busqueda se almacenan aqui

# Se recorre la lista de resultados y se almacenan en la lista

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

'''
Metodo que realiza la busqueda en google
@param query, busqueda que se desea realizar
@return una lista con todos los htmls encontrados en la busqueda
'''
def busqueda():
    query = input("Busqueda: ")
    busquedas = []
    for j in search(query, tld="com", num = 10, stop = 10, pause = 3):
        busquedas.append(j)
    print(busquedas)
    for j in busquedas:  
        try:
            url = urlopen(j,context=ctx).read()
            soup = BeautifulSoup(url, "html.parser")
            res = soup.find_all('p')
            print([i.text for i in res])
        except:
            print("No es posible abrir la pagina")
        

busqueda()
    
