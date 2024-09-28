#!/usr/bin/env python
# coding: utf-8

# # Crear un plano cartesiano
# 
# ### Trabajo realizado por: Jessica Naomi Millan Sánchez
# ### Graficación Computacional
# ### Profesora: Hazem Álvarez Rodríguez
# ### Clase del 09 de septiembre de 2024

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[10]:


x1=0
x2=80

y1=0
y2=80

plt.axis([x1,x2,y1,y2]) # Crear un eje 


# In[9]:


x1=0
x2=40

y1=0
y2=40

plt.axis([x1,x2,y1,y2]) # Crear un eje 


# In[12]:


x1=0
x2=40

y1=0
y2=40

# Crear un eje 
plt.axis([x1,x2,y1,y2]) 

# Habilitar el grid
plt.grid(True)
plt.axis('on')
plt.title('Ejemplo')


# In[20]:


x1=0
x2=80

y1=0
y2=80

# Crear un eje 
plt.axis([x1,x2,y1,y2]) 

# Habilitar el grid
plt.grid(True)
plt.axis('on')
plt.title('Ejemplo')

dx=5
dy=5

for x in np.arange(x1,x2,dx):
    for y in np.arange(y1,y2,dy):
        plt.scatter(x,y,s=1.5, color='lightgray')        


# In[23]:


x1=0
x2=80

y1=0
y2=80

# Crear un eje 
plt.axis([x1,x2,y1,y2]) 

# Habilitar el grid
plt.grid(True)
plt.axis('on')
plt.title('Ejemplo')

dx=1
dy=1

for x in np.arange(x1,x2,dx):
  for y in np.arange(y1,y2,dy):
      plt.scatter(x,y,s=1.5, color='lightgray')  


# In[27]:


x1=0
x2=80

y1=0
y2=80

# Crear un eje 
plt.axis([x1,x2,y1,y2]) 

# Habilitar el grid
plt.grid(True)
plt.axis('on')
plt.title('Ejemplo')

dx=5
dy=5

for x in np.arange(x1,x2,dx):
    for y in np.arange(y1,y2,dy):
        plt.scatter(x,y,s=1.5, color='lightgray')  
        
        # x, y, incremento, abcisa, longitud, ancho, color
plt.arrow(0,80,10,0,head_length=4, head_width=4, color='k')


# ## Actividad

# Graficar el vector ()

# In[44]:


x1=0
x2=20

y1=0
y2=20

# Crear un eje 
plt.axis([x1,x2,y1,y2]) 

# Habilitar el grid
plt.grid(True)
plt.axis('on')
plt.title('Ejemplo')

dx=5
dy=5

for x in np.arange(x1,x2,dx):
    for y in np.arange(y1,y2,dy):
        plt.scatter(x,y,s=1.5, color='lightgray')  
        
        # x, y, incremento, abcisa, longitud, ancho, color
plt.arrow(6,7,-3,-5,head_length=1, head_width=1, color='k')
plt.arrow(11,13,5,0,head_length=1, head_width=1, color='k')
plt.arrow(0,1,5,0,head_length=1, head_width=1, color='k')

