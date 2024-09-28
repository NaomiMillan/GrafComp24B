#!/usr/bin/env python
# coding: utf-8

# # Suma de Vectores
# 
# ### Trabajo realizado por: Jessica Naomi Millan Sánchez
# ### Graficación Computacional
# ### Profesora: Hazem Álvarez Rodríguez
# ### Clase del 23 de septiembre de 2024

# Graficar los vectores vistos en clase:
# 
# A = (2,4)
# 
# B = (-6,-2)
# 
# C = (2, -7)
# 
# 
# Encontrar el vector resultante de la suma de los 3 vectores A, B y C

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


# x, y, incremento, abcisa, longitud, ancho, color
plt.arrow(0,0,2,4,head_length=0.5, head_width=0.5, color=(26/255,184/255,243/255), width=0.05)
plt.arrow(2,4,-6,-2,head_length=0.5, head_width=0.5, color=(23/255,25/255,136/255), width=0.05)
plt.arrow(-4,2,2,-7,head_length=0.5, head_width=0.5, color=(101/255,15/255,193/255), width=0.05)
plt.arrow(-2,-5,2,5,head_length=0.5, head_width=0.5, color=(100/255,100/255,100/255), width=0.05)

plt.plot([], [], color=(26/255, 184/255, 243/255), label='A (2,4)')
plt.plot([], [], color=(23/255, 25/255, 136/255), label='B (-6,-2)')
plt.plot([], [], color=(101/255,15/255,193/255), label='C (2,-7)')
plt.plot([], [], color=(100/255,100/255,100/255), label='A+B+C(-2,-5)')

plt.legend(loc='upper left')


# In[33]:


x1=-7
x2=7
y1=-7
y2=7

# Crear el eje 
plt.axis([x1,x2,y1,y2]) 

# Habilitar el grid
plt.grid(True)
plt.axis('on')
plt.title('Actividad')
       


# In[42]:


x1=-7
x2=7
y1=-7
y2=7

# Crear el eje 
plt.axis([x1,x2,y1,y2]) 

# Habilitar el grid
plt.grid(True)
plt.axis('on')
plt.title('Actividad')
       
        # x, y, incremento, abcisa, longitud, ancho, color
plt.arrow(0,0,2,4,head_length=0.5, head_width=0.5, color=(26/255,184/255,243/255), width=0.05)
plt.arrow(2,4,-6,-2,head_length=0.5, head_width=0.5, color=(23/255,25/255,136/255), width=0.05)
plt.arrow(-4,2,2,-7,head_length=0.5, head_width=0.5, color=(101/255,15/255,193/255), width=0.05)
plt.arrow(0,0,-2,-5,head_length=0.5, head_width=0.5, color=(100/255,100/255,100/255), width=0.05)

plt.text(1.5,2,'A = (2,4)', fontweight="bold")
plt.text(-1.5,4,'B = (-6,-2)', fontweight="bold")
plt.text(-5.5,-1,'C = (2,-7)', fontweight="bold")
plt.text(0,-2,'A+B+C = (-2,-5)', fontweight="bold")

