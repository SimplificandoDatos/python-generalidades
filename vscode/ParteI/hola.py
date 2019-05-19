#%%
#Asignar valor a una variable
a = 3
#%%
#Mostrar el valor de una variable
a
#%%
#Crear una lista
d = [3,1,2,5,4]
#%%
#
for i in range(5):
    print('i es : ',i)
    print('2**i - 1 es: ', 2**i - 1)
#%%[markdown]
#Texto normal
#
# No olvides suscribirte a Simplificando Datos
#%%[markdown]
# Texto con formato
#
# No olvides *suscribirte* a **Simplificando Datos**
#%%[markdown]
# Texto de cabacera 1
# # No olvides suscribirte a Simplificando Datos

#%%[markdown]
# Texto de cabacera 2
# ## No olvides suscribirte a Simplificando Datos

#%%[markdown]
# Texto de cabacera 3
# ### No olvides suscribirte a Simplificando Datos

#%%[markdown]
#Ejemplo de una celda con f?rmula
#
#$e^{i\pi} + 1 = 0$
#%%[markdown]
# ## Crear un gr?fico
# Ejemplo tomado de [Matplolib:Simple Plot](https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html)
#%%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
