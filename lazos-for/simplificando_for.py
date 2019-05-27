#%%[markdown]
# # Simplificando el uso de los lazos for
#%%[markdown]
# ## Uso simple de for
# Imprimir cada uno de los elementos de una lista
#%%
for i in range(5):
    print('i es : ',i)
#%%[markdown]
# ## Operando con listas
# Obtener la suma de los cuadrados de los 
#
# elementos de una lista
#%%[markdown]
# ### Forma tradicional
#%%
x = [1, 3, 5, 7, 9]
suma_cuadrados = 0

for i in range(len(x)):
    suma_cuadrados += x[i]**2
    print(suma_cuadrados)
#%%[markdown]
# ### Un poco m?s pythonista
#%%
x = [1, 3, 5, 7, 9]
suma_cuadrados = 0

for y in x:
    suma_cuadrados += y**2
    print(suma_cuadrados)
#%%[markdown]
# ### La forma pythonista
# [***List comprehension***](https://docs.python.org/3/tutorial/datastructures.html)
#
# #### "Una forma m?s concisa y de f?cil lectura"
#%%
x = [1, 3, 5, 7, 9]
suma_cuadrados = sum([y**2 for y in x])
print(suma_cuadrados)
#%%[markdown]
# ## Uso de for e if
# ### Forma tradicional
#%%
x = [2, 4, 1, 8, 12, 3, 10, 15, 20, 5]
lista = []

for i in x:
    if i > 4:
        lista.append(i)
lista
#%%[markdown]
# ### La forma pythonista
#%%
x = [2, 4, 1, 8, 12, 3, 10, 15, 20, 5]
lista = [i for i in x if i > 4]
lista
#%%[markdown]
# ## Uso de for, if y else
# ### Forma tradicional
#%%
lista = []
x = [-2, -4, 1, 8, -12, 3, -10, 15, 20, 5]

for i in x:
    if i < 0:
        lista.append(i)
    else:
        lista.append(i * -1)
lista
#%%[markdown]
# ### La forma pythonista
#%%
x = [-2, -4, 1, 8, -12, 3, -10, 15, 20, 5]
lista = [i if i < 0 else i * -1 for i in x]
lista
#%%[markdown]
# # Un poco de spam...
# ## NO OLVIDES SUSCRIBIRTE Y COMPARTIR EL VIDEO
# ### GRACIAS