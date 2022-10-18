try:
    from googlesearch import search
    from bs4 import BeautifulSoup
    import ssl
    from urllib.request import urlopen
except ImportError:
    print("One module is missing found")
# Que se va a buscar
query = input("Busqueda: ")
# Los links resultantes de la busqueda se almacenan aqui
busquedas = []
# Se recorre la lista de resultados y se almacenan en la lista
for j in search(query, tld="com", num = 10, stop = 10, pause = 3):
    busquedas.append(j)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

'''
Metodo que realiza la busqueda en google
@param query, busqueda que se desea realizar
@return una lista con todos los htmls encontrados en la busqueda
'''
def busqueda(query):
    return None
    
# Se realiza un analisis del html del documento analizado
'''
for j in busquedas:
    url = urlopen(j,context=ctx).read()
    res = BeautifulSoup(url, "html.parser")
    print(res('a'))
'''
    
