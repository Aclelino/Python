#!/usr/bin/env python
# coding: utf-8

# In[82]:


''' Relogio v1 by Aclelino Dev ...1 de junho de 2022 '''

import time

class Relogio():
    
    def _init_(self):
        pass
        
    # Função de configurar a hora
    
    def ajuste(self,h,m):

        self.s = 0
        self.m = m
        self.h = h 
        
        
    # Estrutura de Repetição
        while True:
            
    # Tempo de pause em looop
            
            time.sleep(1.0)
            
    # Imprimi os valor na tela no Loop     
    
            print( self.h,":",self.m,":",self.s)
    
    # ajuta o tempo em segundo 
    
            if  self.s <=59:
                self.s += 1
                
                if self.s == 60:
                    self.m += 1
                    self.s = 0
                    
                
    # ajuta o tempo em minutos
            
            if self.m >= 60:
                self.h += 1       
                self.m = 0
                
    # ajuta o tempo em Horas   
    
            if self.h >=24 :
                self.h = 0


# In[ ]:


# Abrir a classe relogio 

relod = Relogio() 

# Receber o valor em inteiro do horario a ajustar

h = int(input("Horas: "))
m = int(input("Minutos: "))

# execultar a classe com o dados do Horario ajustado 

relod.ajuste(h,m)


# In[ ]:




