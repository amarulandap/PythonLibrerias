# -*- coding: utf-8 -*-

#importar los paquetes necesarios
#al instalar anaconda, se instalan algunos, pero otros no

#paquete para manipular archivos csv
import csv

#tabulate sirve para mostrar datos en pantalla con una bonita organizadción
#como no lo tenía instalado, abrir el prompt de anaconda como administrador y ejecutar  
# conda install -c conda-forge tabulate
from tabulate import tabulate

#pandas es una librería para manejar y analizar datos, es muy utilizado en ciencia de datos y machine learning
#una de sus principaesl características es el uso de dataframes, que optimizan y hacen transparente varias tareas
#asociadas al manejo de datos (matrices)
import pandas as pd

#Es la base de pandas y está también hecho para el manejo de vactores y matrices
import numpy as np



lista = []

#csv

#ejemplo de lectura de un archivo csv con un reader
with open('L:/0_Descargas/Documentación/semana 6/datos.csv', newline='') as File:
    reader = csv.reader(File) 
    for row in reader:
        #print(row)
        lista.append(row)

x = len(lista[0])
    for row in Lista[0:15]:
    	for col in range (0, x):
	    print(row[0], end = "   ")
    	print ()  

#for row in lista:
        print(row[0], row[1])

lista = []
#ejemplo de lectura de un archivo csv con DictReader 
with open('L:/0_Descargas/Documentación/semana 6/datos.csv', newline='') as File:
    reader = csv.DictReader(File)
    for row in reader:
        lista.append(row)

for row in lista [0:10]:
        print(row['nombre'], row['apellido'])
    


#tabulate

tabla = [["Sol",696000,1989100000],["Tierra",6371,5973.6], ["Luna",1737,73.5],["Marte",3390,641.85]]

print(tabulate(tabla))

print(tabulate({"Name": ["Alice", "Bob"], "Age": [24, 19]}, headers="keys"))

table = [["spam",42],["eggs",451],["bacon",0]]
headers = ["item", "qty"]
print(tabulate(table, headers, tablefmt="plain"))


print(tabulate(lista[0:15],  headers="keys"))

new_list = []
for item in lista:
    new_list.append({'id':item['id'], 'nombre':item['nombre']})
print(tabulate(new_list[0:15],  headers="keys"))


##pandas
#https://www.youtube.com/watch?v=gimfTyCNfGw

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
"capital": ["Brasilia", "Moscow", "New Dehli","Beijing", "Pretoria"],
"area": [8.516, 17.10, 3.286, 9.597, 1.221],
"popula􀆟on": [200.4, 143.5, 1252, 1357, 52.98] }


brics = pd.DataFrame(dict)
print(brics)


xxx = pd.DataFrame(lista)
print(xxx)


#numpy
#https://www.youtube.com/watch?v=WxJr143Os-A
#https://www.youtube.com/watch?v=aqIMhiialq0

x = np.array([5.6, 7.3, 7.7, 2.3, 4.2, 9.2])
decimales = np.array([0.3])

print(x+decimales)

#decimales = np.array([0.3, 0.2])
#print(x+decimales) ##error


z = np.array([51.6, 7.32, 17.75, 42.23, 4.112, 93.22])

print(z)
print(z.max()) # Valor máximo de los elementos del array
print(z.min()) # Valor mínimo de los elementos del array
print(z.mean()) # Valor medio de los elementos del array
print(z.std()) # Desviación estándar de los elementos del array
print(z.sum()) # Suma de todos los elementos del array
print(np.median(z)) # Mediana de los elementos del array

