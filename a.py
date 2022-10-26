from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
import analisisSentimiento as asen
import ssl 
"""try:
    from googlesearch import search
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import pandas as pd
    import numpy as np
    import analisisSentimiento as asen
    import ssl 
    
except ImportError:
    print("One module is missing found")"""

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
    busquedas = {}
    df = pd.DataFrame(columns=['Link', 'Titulo', 'Texto'])
    for j in search(query, tld="com", num = 10, stop = 1, pause = 3):
        busquedas.update({j:""})
    print(busquedas.keys())
    df['Link']= busquedas.keys()
    resultados = []
    titulos = []
    for j in busquedas.keys():  
        try:
            url = urlopen(j,context=ctx).read()
            soup = BeautifulSoup(url, "html.parser")
            res = soup.find_all('p')
            tit = soup.find_all('h1')
            tit1 = [i.text for i in tit]
            titulos.append(str(tit1))
            res1 = [i.text for i in res]
            print(str(res1))
            resultados.append(str(res1))#[0:500]
        except OSError:
            print("No es posible abrir la pagina"+ OSError)
    df['Texto'] = np.array(resultados)
    df['Titulo'] = np.array(titulos)
    return df
print(busqueda())
