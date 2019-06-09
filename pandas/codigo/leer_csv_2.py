# -*- coding: utf-8 -*-
#%%[markdown]
# # Simplificando pandas, lectura y escritura de archivos II
#%%[markdown]
# Importamos las librerias a utilizar
#%%
import os
from pathlib import Path
import glob
import numpy as np
import pandas as pd
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
# ## Extraer informacion de varios archivos
#%%
# Lista de los nombres de los archivos de interes
lista_csv = [f for f in dir_entra.glob("*.csv")]
lista_csv
#%%
# Lista final de los nombres de los archivos de interes
lista_csv = [f for f in dir_entra.glob("*.csv") if "ejemplo.csv" not in str(f)]
lista_csv
#%%[markdown]
# ### Dataframe vacío
clima = pd.DataFrame({'time':[],'precipIntensity':[],
                    'temperature':[],'apparentTemperature':[],
                    'dewPoint':[],'humidity':[],'pressure':[],
                    'windSpeed':[],'cloudCover':[]})
columnas = ['time','precipIntensity','temperature','apparentTemperature',
            'dewPoint','humidity','pressure','windSpeed','cloudCover']
#%%[markdown]
# Comenzamos a cargar los datos
#%%
for archivo in lista_csv:
    clima_temp = pd.read_csv(archivo)
    # Seleccionamos las columnas de interes
    clima_temp = clima_temp[columnas]
    # Unimos Dataframnes
    clima = pd.concat([clima, clima_temp], join='inner', axis=0)
    clima = clima[columnas]
clima = clima.set_index('time')
#%%[markdown]
# ### Verifiquemos el archivo creado
#%%
clima.head()
#%%
clima.tail()
#%%
clima.shape
#%%
clima.dtypes
#%%[markdown]
# ## Guardemos la información
#%%
clima.to_csv(dir_inter / 'clima.csv')
#%%[markdown]
# ## Cargar varios archivos, modificarlos y luego 
# ## guardarlos individualmente
#%%
for archivo in lista_csv:
    clima_temp = pd.read_csv(archivo)
    # Seleccionamos las columnas de interes
    clima_temp = clima_temp[columnas]
    clima_temp = clima_temp.set_index('time')
    archivo2 = dir_inter / ''.join([archivo.name[:6], '.csv'])
    clima_temp.to_csv(archivo2)

#%%
