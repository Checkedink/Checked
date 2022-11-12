
# importamos el modulo pyplot, y lo llamamos plt

import matplotlib.pyplot as plt

#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'




#tambien importamos numpy ya que lo usamos para crear y manipular matrices
import numpy as np

#tamaño de las matrices a visualizar
size=(20,30)

# Una matriz de ceros. 
imagen_negra = np.random.randint(2, size=(20,30))
#visualizamos la matriz
#Se ve como una imagen negra, ya que todos los elementos (pixeles) tienen intensidad 0
plt.imshow(imagen_negra,vmin=0,vmax=1)
# (es necesario indicar vmin y vmax para que pyplot sepa que el minimo es 0 y el maximo 1)
# (solo imagenes escala de grises)
plt.show()