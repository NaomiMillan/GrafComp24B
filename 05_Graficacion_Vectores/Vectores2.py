#!/usr/bin/env python
# coding: utf-8

# # Graficar Vectores y sus componentes
# 
# ### Trabajo realizado por: Jessica Naomi Millan Sánchez
# ### Graficación Computacional
# ### Profesora: Hazem Álvarez Rodríguez
# ### Clase del 11 de septiembre de 2024

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[22]:


x1=-9
x2=9
y1=-9
y2=9

# Crear el eje 
plt.axis([x1,x2,y1,y2]) 

# Habilitar el grid
plt.grid(True)
plt.axis('on')
plt.title('Ejercicio 1')
       
        # x, y, incremento, abcisa, longitud, ancho, color
plt.arrow(0,0,3,4,head_length=0.5, head_width=0.5, color=(26/255,184/255,243/255), width=0.05, linestyle=":")
plt.arrow(0,0,-5,2,head_length=0.5, head_width=0.5, color=(23/255,25/255,136/255), width=0.05, linestyle=":")
plt.arrow(0,0,2,-4,head_length=0.5, head_width=0.5, color=(101/255,15/255,193/255), width=0.05, linestyle=":")
plt.arrow(0,0,-7,-3,head_length=0.5, head_width=0.5, color=(100/255,100/255,100/255), width=0.05, linestyle=":")


plt.plot([0,3], [0,0], color=(26/255, 184/255, 243/255), label='A (3,4)')
plt.plot([3,3], [0,4], color=(26/255, 184/255, 243/255))
plt.plot([0,-5], [0,0], color=(23/255, 25/255, 136/255), label='B (-5,2)')
plt.plot([-5,-5], [0,2], color=(23/255, 25/255, 136/255))
plt.plot([0,2], [0,0], color=(101/255,15/255,193/255), label='C (2,-4)')
plt.plot([2,2], [0,-4], color=(101/255,15/255,193/255))
plt.plot([0,-7], [-3,-3], color=(100/255,100/255,100/255), label='D (-7,-3)')
plt.plot([0,0], [0,-3], color=(100/255,100/255,100/255))

plt.legend(loc='upper left')

plt.text(1,2,'A', fontweight="bold")
plt.text(-2,1.2,'B', fontweight="bold")
plt.text(0.3,-2,'C', fontweight="bold")
plt.text(-3,-1,'D', fontweight="bold")

plt.text(1.3,0.2,'Ax', fontstyle="italic", size='small')
plt.text(3,2,'Ay', fontstyle="italic", size='small')

plt.text(1,-0.5,'Cx', fontstyle="italic", size='small')
plt.text(2,-2,'Cy', fontstyle="italic", size='small')

plt.text(-3,0.2,'Bx', fontstyle="italic", size='small')
plt.text(-6,1,'By', fontstyle="italic", size='small')

plt.text(-2,-3.8,'Dx', fontstyle="italic", size='small')
plt.text(-0.6,-1.6,'Dy', fontstyle="italic", size='small')

