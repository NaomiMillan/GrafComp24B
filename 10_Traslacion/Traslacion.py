#!/usr/bin/env python
# coding: utf-8

# # Traslación, Rotación y Escalado de Figuras
# 
# ### Trabajo realizado por: Jessica Naomi Millan Sánchez
# ### Graficación Computacional
# ### Profesora: Hazem Álvarez Rodríguez
# ### Clase del 09 de octubre de 2024

# In[4]:


import matplotlib.pyplot as plt
import numpy as np


# ## Escalado

# In[9]:


esc = 3
esc2 = 5

trianguloX = np.array([1, 1.5, 2, 1])
trianguloY = np.array([1, 2, 1, 1])

tX = esc * trianguloX
tY = esc2 * trianguloY

# escalado
plt.plot(tX, tY)
# original
plt.plot(trianguloX, trianguloY)


# In[11]:


esc = 6
esc2 = 6

cuadradoX = np.array([1, 1, 2, 2, 1])
cuadradoY = np.array([1, 2, 2, 1, 1])

cX = esc * cuadradoX
cY = esc2 * cuadradoY

# escalado
plt.plot(cX, cY)
# original
plt.plot(cuadradoX, cuadradoY)


# ## Rotación

# In[22]:


theta = np.radians(30)

trianguloX = np.array([1, 1.5, 2, 1])
trianguloY = np.array([1, 2, 1, 1])

tX = np.cos(theta) * trianguloX - np.sin(theta) * trianguloY
tY = np.sin(theta) * trianguloX + np.cos(theta) * trianguloY

# rotacion
plt.plot(tX, tY)
# original
plt.plot(trianguloX, trianguloY)


# In[29]:


theta = np.radians(20)

cuadradoX = np.array([1, 1, 2, 2, 1])
cuadradoY = np.array([1, 2, 2, 1, 1])

tX = np.cos(theta) * cuadradoX - np.sin(theta) * cuadradoY
tY = np.sin(theta) * cuadradoX + np.cos(theta) * cuadradoY

# rotacion
plt.plot(tX, tY)
# original
plt.plot(cuadradoX, cuadradoY)


# ## Traslación

# In[14]:


tras = 3
tras2 = 5

trianguloX = np.array([1, 1.5, 2, 1])
trianguloY = np.array([1, 2, 1, 1])

tX = tras + trianguloX
tY = tras2 + trianguloY

# traslación
plt.plot(tX, tY)
# original
plt.plot(trianguloX, trianguloY)


# In[20]:


tras = -2
tras2 = 2

cuadradoX = np.array([1, 1, 2, 2, 1])
cuadradoY = np.array([1, 2, 2, 1, 1])

cX = tras + cuadradoX
cY = tras2 + cuadradoY

# traslación
plt.plot(cX, cY)
# original
plt.plot(cuadradoX, cuadradoY)

