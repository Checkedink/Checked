"""
Primera parte reconocimiento de cadenas por porcentages 
"""

from fuzzywuzzy import process #importa el fuzzy wuzzy

def conincidence(options:list, match:str)->tuple: #busca la coincidencia más cercana
    """Ratios = process.extract()""" # esto se deja por si queremos generar un promedio.
    highest = process.extractOne(options,match)
    return highest
