"""
Primera parte reconocimiento de cadenas por porcentages 
"""
import nltk.corpus
import re
from fuzzywuzzy import process #importa el fuzzy wuzzy
import nltk
import numpy as np
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer 
from sentence_transformers.util import cos_sim
from nltk import tokenize

nltk.download('stopwords')
nltk.download('punkt')
model= SentenceTransformer('all-mpnet-base-v2')
"""test= open("test.txt", mode="r", encoding="utf8")
text= test.read()
print(text)
test.close()"""
def conincidence_by_dp(options:list, match:str)->tuple: #busca la coincidencia más cercana
    """Ratios = process.extract()""" # esto se deja por si queremos generar un promedio.
    highest = process.extractOne(options,match)
    return highest
#este programa da la similaridad a partir de machien learning y transformar las palabras en vectores, que con el modelo 
# se processa, devuelve una matriz de n * n donde n son la cantidad de palabras que se le da  y basicamente es la coincidencia de cada palabra con cada palabra 
#si lo crea una y otra vez pero creo que hay limitaciones y por ende pues pasa esto 
def coincidence_by_embeddings(palabras,query):
    palabras.append(query[0])
    embeddings= model.encode(palabras)
    sim= np.zeros((len(palabras), len(palabras)))
    for i in range(len(palabras )):
        sim[i:,i]=cos_sim(embeddings[i],embeddings[i:])
    return sim
def extract_tokenize_clean(text):
    text = text.lower()
    stop = stopwords.words('english')
    text = " ".join([word for word in text.split() if word not in (stop)])
    text= re.sub("(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    tokens = nltk.sent_tokenize(text)
    return tokens

print(extract_tokenize_clean("fuck you Gonorrea 1975 //"))

