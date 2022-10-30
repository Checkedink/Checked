"""
Primera parte reconocimiento de cadenas por porcentages 
"""

from fuzzywuzzy import process #importa el fuzzy wuzzy
import numpy as np
from sentence_transformers import SentenceTransformer 
from sentence_transformers.util import cos_sim
from nltk import tokenize

def conincidence_by_dp(options:list, match:str)->tuple: #busca la coincidencia más cercana
    """Ratios = process.extract()""" # esto se deja por si queremos generar un promedio.
    highest = process.extractOne(options,match)
    return highest
#este programa da la similaridad a partir de machien learning y transformar las palabras en vectores, que con el modelo 
# se processa, devuelve una matriz de n * n donde n son la cantidad de palabras que se le da  y basicamente es la coincidencia de cada palabra con cada palabra 
def coincidence_by_embeddings(palabras):
    model= SentenceTransformer('all-mpnet-base-v2')
    embeddings= model.encode(palabras)
    sim= np.zeros((len(palabras), len(palabras)))
    for i in range(len(palabras )):
        sim[i:,i]=cos_sim(embeddings[i],embeddings[i:])
    return sim
"""def get_words(text, ):
    tokenize"""