from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
import analisisSentimiento as asen
import ssl 
import coincidence 
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
    query = insertQuery()
    print("Verificando... Por favor espere...\n")
    busquedas = {}
    df = pd.DataFrame(columns=['Link', 'Titulo', 'Texto'])
    for j in search(query, tld="com", num = 10, stop = 10, pause = 3):
        busquedas.update({j:""})
    printFuentes(busquedas.keys())
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
            resultados.append(str(res1)[0:500])
        except OSError:
            print("No es posible abrir la pagina")
    df['Texto'] = np.array(resultados)
    df['Titulo'] = np.array(titulos)
    return df

def busqueda_por_sentimiento():
    df = busqueda()
    df['Sentimiento'] = df['Texto'].apply(asen.analisisSentimiento)
    print(df)
    media = df['Sentimiento'].mean()
    if(media<3):
        return("Es probable que el dato sea falso")
    elif(media>3):
        return("Es probable que el dato sea verdadero")
    else:
        return("Es probable que el dato sea dudoso")

def busqueda_mod():
    query = insertQuery()
    busquedas = {}
    for j in search(query, tld="com", num = 5, stop = 5, pause = 3):
        busquedas.update({j:""})
    printFuentes(busquedas.keys())
    query=coincidence.extract_tokenize_clean(query)
    final = []
    for j in busquedas.keys():  
        try:
            url = urlopen(j,context=ctx).read()
            soup = BeautifulSoup(url, "html.parser")
            res = soup.find_all('p', text=False,recursive=True)
            res1 = [i.text for i in res]
            final.append(res1)
            for tex in final[0]:
                tokens=coincidence.extract_tokenize_clean(tex)
                if len(tokens) != 0:
                    res = coincidence.coincidence_by_embeddings(tokens, query)
                    for j in range(len(res)-1):
                        element=res[-1][j]
                        if element > 0.8:
                            return True
        except Exception as e: print(e)
    return False

def insertQuery():
    print("\n"+"*"*44+"\n")
    print( "Por favor inserte la información a consultar\n")
    print("*"*44+"\n")
    query= input("-> ")
    print("\n")
    return query

def printFuentes(fuentes):
    print("-"*44+"\n"+"Fuentes consultadas\n")
    for fuente in fuentes:
        print("-> "+ fuente +"\n" )

def main():
    #print(busqueda_mod())
    while True:
        resultado=busqueda_mod()
        if resultado:
            print("*** La información introducida es verdadera ***\n")
        else:
            print("*** La información introducida es falsa ***\n")
        # print(busqueda_por_sentimiento())
        # ctrl+c en la consola para detener

main()
