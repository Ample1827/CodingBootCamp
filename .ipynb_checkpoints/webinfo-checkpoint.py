# %% [markdown]
# Here we only need the data to scrap website + _Pandas_
# - Nombre del tecnológico
# - Estado
# - Clave oficial
# - Modalidad (Escolarizada / No escolarizada)
# - Grado que otorga
# - Carreras y módulos de especialidad
# - url of the website / tecnológico
# 
# **Consultas que debe permitir el sistema**
# 
# ¿Qué tecnológicos ofrecen la modalidad no escolarizada?
# 
# ¿Qué tecnológicos comparten la misma carrera?
# 
# ¿Cuántos tecnológicos son de tipo federal o estatal?
# 
# ¿Cuáles son los módulos de especialidad disponibles por carrera (solo el nombre)?

# %%
from bs4 import BeautifulSoup
import requests
import pandas as pd

# %%
url = 'https://www.tecnm.mx/json/tecnm_institutos.json'
response = requests.get(url)
data = json.loads(response.content.decode('utf-8-sig'))

# %%
print(type(data))
print(len(data))
print(data[0]) 

# %%
url = 'https://www.tecnm.mx/?vista=Licenciaturas'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# %%
print(soup)

# %%
data = response.json()

# %%
print(table)

# %%


# %%


# %%



