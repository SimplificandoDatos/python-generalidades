# -*- coding: utf-8 -*-
#%%[markdown]
# # Simplificando pandas, lectura y escritura de archivos I
#%%[markdown]
# Importamos las librerias a utilizar
#%%
import os
from pathlib import Path
import glob
import numpy as np
import pandas as pd
#%%[markdown]
# # ¿Qué es pandas?
#
# [**pandas**](https://pandas.pydata.org/)
#
# **pandas** es una librería de código abierto con licencia BSD que 
# proporciona estructuras de datos de alto rendimiento y fáciles de usar 
# y herramientas de análisis de datos para el lenguaje de programación Python.
#%%[markdown]
# ## Estructuras de pandas
#%%[markdown]
# ### Series
#
# Arreglo unidimensional (vector), homogéneo y etiquetado.
#%%[markdown]
# Creación de una Serie con una lista de valores 
#%%
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=['a', 'b', 'c', 'd', 'e', 'f'])
s
#%%[markdown]
#  ### Dataframes
#
# Estructura tabular bidimensional, de tamaño modificable, etiquetada
#  
# con columnas potencialmente heterogéneas.
#%%[markdown]
# Creación de un DataFrame usando un array de NumPy, fecha como índice (index) 
# y  columnas etiquetadas:
#%%
dates = pd.date_range('20180501', periods=6)
dates
#%%
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df
#%%[markdown]
# Creación de un DataFrame usando diccionarios (dic)
#%%
df2 = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'}, index = ['f', 'g', 'h', 'i'])
df2
#%%[markdown]
# # Módulo pathlib
#%%
# directorio actual
dir_prin = Path.cwd()
dir_prin
#%% 
# directorio con los datos
dir_entra = dir_prin/'entradas'
dir_entra
#%%
# directorio con los datos intermedios
dir_inter = dir_prin /'intermedios'
dir_inter 
#%%
# directorio con los datos finales
dir_salid = dir_prin / 'salidas'
dir_salid 
#%%[markdown]
# # Lectura desde archivos csv
#%%[markdown]
# ## Un archivo
#%%
datos = pd.read_csv(dir_entra / 'ejemplo.csv')
#%%
# Observar las primeras filas
datos.head()
#%%
datos = pd.read_csv(dir_entra / 'ejemplo.csv', skiprows=5)
datos.head(10)
#%%
# Observar las últimas filas
datos.tail(6)
#%%
# Dimensiones del Dataframe
datos.shape
#%%
# Nombre de las columnas
datos.columns
#%%
# Index
datos.index
#%%
# Información de las columnas
datos.info()
#%%
# Tipos de datos
datos.dtypes
#%%[markdown]
# Más sobre [tipos de datos en python](https://data-flair.training/blogs/python-variables-and-data-types/)
#%%[markdown]
# ### Eliminar una columna y cambiar el index
#%%
datosv2 = datos.drop(['Unnamed: 0'], axis=1)
datosv2 = datosv2.set_index('time')
datosv2.head()
#%%
# Resumen estadístico
datosv2.describe()
#%%
# Valor de correlación lineal entre columnas
datosv2.corr()