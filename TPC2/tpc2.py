# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:00:28 2021

@author: marta
"""

#TPC2 - Adivinhe o número de 0 a 100

def adivinhe():
    ne=0
    nd=100
    nm=int(100/2)
    t=1
    print(nm)
    r=input('É este o seu número?')
    
    while(r=='não' or r=='no'):
        r2=input('É acima ou abaixo do número?')
        if(r2=='acima'):
            ne=nm
        elif(r2=='abaixo'):
            nd=nm
        s=ne+nd
        nm=int(s/2)
        print(nm)
        r=input('É este o seu número?')
        t=t+1
    if(r=='sim' or r=='yes'):
        print('Acertou o número!')
        print('Acertei em', t, 'tentativas!')
adivinhe()        
        
