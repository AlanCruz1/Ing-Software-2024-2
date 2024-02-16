import numpy as np
from matplotlib import pyplot as plt

#LIMITANDO EL PLANO EN BASE AL EJE X
x= np.linspace(-10,10)
#LAS FUNCIONES SENO Y COSENO
y_seno = np.sin(x)
y_coseno = np.cos(x)

#GRAFICACIÓN DE SENO
plt.plot(x,y_seno)
plt.plot(x, y_seno, label='sen(x)', color='pink')

#GRAFICACIÓN DE COSENO
plt.plot(x,y_coseno)
plt.plot(x, y_coseno, label='cos(x)', color='yellow')

#MOSTRAR GRÁFICA 
plt.show()