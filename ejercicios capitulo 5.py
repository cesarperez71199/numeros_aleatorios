# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:22:55 2023

@author: Cesar Perez
"""

#Ejercicios capitulo 5 
# 1

"""
a= "continente"
b="americano"

print(a+ " "+b)

"""

#2

import random

nombre=input("")

numero_elegido=int(input)

print("Okey", nombre, "adivina el numero entre 1 y 20", numero_elegido)


numero_aleatorio = [random.randint(1, 20)]

contador=0
for numero_elegido in numero_aleatorio:
    if numero_elegido == numero_aleatorio:
        print("felicidades")
        
    elif numero_elegido < numero_aleatorio:
        print("numero bajo")
    
        numero_elegido=int(input("Dame otro numero: "))
    
    else:
        numero_elegido > numero_aleatorio
        print("Numero alto")
        
        numero_elegido= int(input("Dame otro numero"))



