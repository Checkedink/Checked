from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def analisisSentimiento(txt):
    '''
    Instanciar modelo
    '''
    # Crear tokenizador para traer el modelo de analisis de sentimiento
    tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
    # Crear modelo de analsis de sentimiento preentrenado
    model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

    '''
    Codificar y calcular el sentimiento
    '''
    # codificar el texto
    tokens = tokenizer.encode(txt, return_tensors='pt')
    # enviar al modelo
    result = model(tokens)
    return(int(torch.argmax(result.logits))+1)
