#!/usr/bin/env python
# coding: utf-8

# # Ecuaciones Lineales
# 
# ### Trabajo realizado por: Jessica Naomi Millan Sánchez
# ### Graficación Computacional
# ### Profesora: Hazem Álvarez Rodríguez
# ### Clase del 11 de noviembre de 2024

# ## Ejemplo

# In[2]:


import numpy as np


# In[7]:


A4 = np.matrix([[3,2,-1],[2,-2,4],[-1,0.5,-1]])
b4 = np.matrix([[1],[-2],[0]])


# In[10]:


x4 = (A4**-1)*b4
determinante4 = np.linalg.det(A)


# In[11]:


# Mostrar los resultados
print("Forma matricial A x = b:")
print("Matriz A:")
print(A4)
print("Vector b:")
print(b4)
print("\nDeterminante de A:", determinante4)
print("\nValor de x:")
print(x4)


# ## Actividad

# ### 1. A = (9)

# In[6]:


A = np.matrix([[9]])

print("this is A\n",A)
det = np.linalg.det(A)
print("this is the determinante\n",det)


# ### 2. B = ([4 -1]  [-2 0])

# In[3]:


A = np.matrix([[4, -1],[-2, 0]])

print("this is A\n",A)
det = np.linalg.det(A)
print("this is the determinante\n",det)


# ### 2. C = ([5 0 2]  [3 1 1] [0 1 2])

# In[4]:


A = np.matrix([[5, 0, 0], [3, 1, 1],[0, 1, 2]])

print("this is A\n",A)
det = np.linalg.det(A)
print("this is the determinante\n",det)

