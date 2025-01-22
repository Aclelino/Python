#!/usr/bin/env python
# coding: utf-8

# In[9]:



#importa o modeulo os
import os


# In[10]:


#Local da pasta de Imagens 
path = '/home/aclelino/Imagens/3d'


# In[11]:


# ler a lista do local Path
lista = os.listdir(path)


# In[12]:


# Função para Renomear 

def renomear():

    i = 1
    for nome in lista:
        new_nome = ('klnimg{}.jpg'.format(i))
        os.rename(nome, new_nome)
        i += 1
renomear()


# In[ ]:




