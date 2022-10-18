try:
    from googlesearch import search
    from bs4 import BeautifulSoup
    import ssl
    from urllib.request import urlopen
except ImportError:
    print("One module is missing found")
query = input("Busqueda: ")
busquedas = []
for j in search(query, tld="com", num = 10, stop = 10, pause = 3):
    busquedas.append(j)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for j in busquedas:
    url = urlopen(j,context=ctx).read()
    res = BeautifulSoup(url, "html.parser")
    print(res('a'))

    
