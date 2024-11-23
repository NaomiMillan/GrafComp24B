#!/usr/bin/env python
# coding: utf-8

# # Núcleo de una matriz
# 
# ### Trabajo realizado por: Jessica Naomi Millan Sánchez
# ### Graficación Computacional
# ### Profesora: Hazem Álvarez Rodríguez
# ### Clase del 11 de noviembre de 2024

# In[3]:


import numpy as np
from scipy.linalg import null_space


# In[4]:


# Definir matrices
matrix1 = np.array([[1, 1, 0], [1, 1, 0]])
matrix2 = np.array([[1, 1, 2], [2, 2, 4], [2, 3, 5]])


# In[5]:


# Cálcula el espacio vacío 
kernel1 = null_space(matrix1)
kernel2 = null_space(matrix2)


# In[7]:


# Mostrar resultados
print("Núcleo de la matriz 1:")
print(kernel1)
print("\nNúcleo de la matriz  2:")
print(kernel2)

