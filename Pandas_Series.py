# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:28:45 2021

@author: Andres Marulanda
"""

import pandas as pd
import numpy as np
from math import sqrt

#Series son matrices unidimensionales(vectores).
#Dataframe son matrices bidimensionales.
#Paneles o datos de 3 dimensiones

#Serie creada a partir de una lista
Numeros_1 = np.random.randint(1, 50, size = 20)
serie_3 = pd.Series(Numeros_1, dtype='int32')
print("serie creada a partir de una lista de números: ")
print(serie_3)

Numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, None, 5, 2, 9, 2, 1, None, 8, 9, 4, 6, 2, np.NaN, 3, 5, np.NaN, 8, 10]
serie_2 = pd.Series(Numeros)
print("serie creada a partir de una lista de números: ")
print(serie_2)

Materias = ['Algebra', 'Español', 'Ciencias Naturales', 'Educación Física', 'Química']
serie_1 = pd.Series(Materias, dtype=('string'))
print("Serie creada a partir de una lista: ")
print(serie_1)

#Serie creada a partir de un diccionario
dict_1 = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5'}
serie = pd.Series(dict_1)
print("'Serie creada a partir de un diccionario: ")
print(serie)

#Conocer el tamaño de la serie
print("\nTamaño de la serie: ",serie.size)

#Acceder a la posición de una serie
#Por posición
print("\nDato de la serie 1 en la posición 2: ",serie_1[2])
#Por indice
print("")
print(serie_1[0:2])

#Métodos de acceso (las filas y las columnas se cuentan desde cero)
print("\nDato en la posición 1 de la serie: ",serie.iloc[2])

#Conocer el número de elementos no nulos en una serie
print("\nNúmero de elementos no nulos en la serie 1: ",serie_1.count())

#Conocer la suma de todos los elementos de la serie
serie_3_sum = serie_3.sum()
print("\nsuma de los elementos de la serie 3: ",serie_3_sum)

#Serie con la suma acumulada de los valores de una serie numérica
print("\nSerie de sumas acumuladas: ")
print(serie_2.cumsum())

#Números de veces que se repite cada elemento de la serie
print("\nNúmero de veces que se repite cada elemento en la serie 2: ")
print(serie_2.value_counts())

#Mínimo valor de los datos de una serie
print("\nMínimo valor de la serie:",serie.min())

#máximo valor de una serie
print("\nMáximo valor de la serie 2: ",serie_2.max())

#Media de los datos de una serie
print("\nMedia aritmética de los datos de la serie 2: ",serie_2.mean())

#Desviacion estándar
print("Desviacion estandar de los datos de la serie ",serie_3.std())

#Resumen de todas las medidas estadisticas
print("\nResumen de las caracteristicas de la serie 3: ")
print(serie_3.describe())

#El procedimiento es similar para todas las operaciones aritméticas
print("")
print(serie_2 % 2)
print("")
print(serie_1 * 3)

#Aplicar funciones de otros modulos a las series
print("\nraiz cuadrada de los elementos de la serie 3: ")
print(serie_3.apply(sqrt))
print("")
print(serie_1.apply(str.upper))

#filtrar una serie
print("\nSerie 3 filtrada: ")   
print(serie_3[serie_3<20])

#Ordenar desceendentemente una lista por indices
print("\Serie ordenada descendentemente: ",serie.sort_index(ascending=False))

#Ordenar la serie de forma ascendente por valores
print("\nSerie 2 ordenada ascendentmente: ",serie_2.sort_values())

#Eliminar los valores nulos de una serie
print("\nLa serie 2 sin valores nulos: ",serie_2.dropna())









