# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 06:25:26 2021

@author: Andres Marulanda
"""

"""INTRODUCCIÓN A PANDAS"""

import numpy as np
import pandas as pd
from math import sqrt

#Crear un dataframe a partir de un diccionario
dict = {"País": ["Brazil", "Russia", "India", "China", "South Africa"],
        "Capital": ["Brasilia", "Moscow", "New Dehli","Beijing", "Pretoria"],
        "Area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "Población": [200.4, 143.5, 1252, 1357, 52.98] }
#Asigna las claves del diccionario como títulos de las columnas
info_paises = pd.DataFrame(dict)
print("\nDataframe a partir de un diccionario: ")
print(info_paises) 

#Crear un Df a partir de una lista de diccionarios
df_2 = pd.DataFrame([{'Nombre':'Andres', 'Edad': '18'}, {'Nombre':'Carlos', 'Edad':'22'},
                      {'Nombre':'Maria', 'Edad':'30'}])
print("\nDF creado a partir de una lista de diccionarios: ")
print(df_2)

#Crear un DF a partir de una lista de listas
lista_1 = [['Andres',40],['Maria',70],['Cristina',45],['Carolina',22]]
df_1 = pd.DataFrame(lista_1, columns=('Nombre','Edad'))
print("\nDF a partir de una lista de listas: ")
print(df_1)

#Forma mas sencilla de crear un DF.
df = pd.DataFrame(np.array([[1,None,3],[4,5,6],[7,8,9],[10,None,12],[13,None,15]]))
print("\nPrimer DF: ")
print(df)

#Crear un dataframe a partir de un arreglo data de Numpy
data = np.array([['', 'Col_1','Col_2'], ['Fila_1', 200, 400], ['Fila_2', 100, 300]])
print("\nDataFrame a partir de un arreglo Np: ")
data_1 = pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:])
print(data_1)

#crear un DF a partir de un array de Numpy
df_3 = pd.DataFrame(np.random.randn(5, 4), columns=['A', 'B', 'C', 'D'])
print("\nDF generado a partir de un array de Np: ")
print(df_3)

#Crear un DF con un fichero CSV o excel
#Para crearlos a partir de ficheros de excel usamos el metodo
#read_excel(fichero.xlsx, sheet_name=hoja, header=n, index_col=m, na_values=no-validos, decimal=separador-decimal) 
df_csv = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv',
                     sep = ';', decimal = ',')
print("\nDF creado a partir de un fichero CSV: ")
print(df_csv.head)

#df.to_csv(fichero.csv, sep=separador, columns=booleano, index=booleano) : 
#Exporta el DataFrame df al fichero fichero.csv en formato CSV usando como separador de los datos 
#la cadena separador. Si se pasa True al parámetro columns se exporta también la fila con los 
#nombres de columnas y si se pasa True al parámetro index se exporta también la columna con los 
#nombres de las filas.

#df.to_excel(fichero.xlsx, sheet_name = hoja, columns=booleano, index=booleano) : 
#Exporta el DataFrame df a la hoja de cálculo hoja del fichero fichero.xlsx en formato Excel. 
#Si se pasa True al parámetro columns se exporta también la fila con los nombres de columnas y si 
#se pasa True al parámetro index se exporta también la columna con los nombres de las filas.

#---------------------------------------------------------------------------

#Conocer la info del DF
print("\nInfo del DF df_2: ",df_2.info())

#Conocer la forma del DF
print("\nForma del primer DF: ",df.shape)

#Conocer el número de elementos del DF
print("\nNúmero de elementos del DF 2: ",df_2.size)

#Conocer el nombre de las columnas de un DF
print("\nNombre de las columnas del DF csv: ",df_csv.columns)

#Conocer los nombres de las filas del DF
print("\nNombre de las filas del DF info_paises: ",info_paises.index)

#Conocer los tipos de datos de las columnas
print("\ntipos de datos de las columnas del DF df_3: ",df_3.dtypes)

#Sub DF con las n primeras filas
print("\nDF df_csv con las 4 primeras filas")
print(df_csv.head(4))

#Sub DF con las n últimas filas
print("\nDF df_csv con las 4 últimas filas")
print(df_csv.tail(4))

#Renombrar las filas y las columnas de un DF
#Para renombrar las filas, se incluyen despues de columns, index={}
print("\nDF df con columnas renombradas: ")
print(df.rename(columns={0:'columna_1', 1:'columna_2', 2:'columna_3'}))

#Reordenar las filas y/o columnas del DF
print("\nDF df con un nuevo orden en las filas: ")
print(df.reindex(index=[4,2,0,5]))

#Métodos de acceso (las filas y las columnas se cuentan desde cero)
#Devuelve el elemento que se encuentra en la fila y columna indicada
print("\nDato en la posición 1-2 del DF data_1: ",data_1.iloc[0, 1])
print("\nDatos de la fila 1: ",data_1.iloc[1,:2])

#Acceso a traves de nombres
print("\nDatos de la fila 1 de data_1: ",info_paises.loc[1])
print("\nDato en la fila 0, columna Nombre: ",df_2.loc[0, 'Nombre'])

#Conocer los datos de una fila, total o parcialmente
print("\ndatos de la fila 1 de DF_3: ",df_3.loc[:2,('A','B','C')])

#Conocer la información de una o varias columnas
print(info_paises[['País', 'Capital']])

#Como seleccionar una columna del DF
print("")
print(df[1])

#Conocer la altura (Número de filas) del DF
print("\nAltura del DF: ",len(info_paises.index))

#Añadir una columna a un DF
print("\nDF 1 con una columna adicional: ")
df_1['Cédula']=pd.Series([123456789, 98765432, 1039865241, 85296354])
print(df_1)

#Operaciones sobre una columna
print("")
print(df_3['A'] * 100)

#Aplicar funciones a columnas
print("\nRaices cuadradas de los elementos del DF: ",df[0].apply(sqrt))

#Conocer las estadisticas del DF por columnas
print("\nEstadisticas del DF_3: ",df_3.describe())

#Conocer el número de elementos no nulos por columna
print("\nNúmero de elementos no nulos del DF_:",df.count())

#Conocer la suma de los datos de cada columna
df_2_sum = df_2.sum()
print("\nSuma de los datos de las columnas del DF_",df_2_sum)

#Conocer la suma acumulada de cada una de las columnas
print("\nSuma acumulada de las columnas del DF_3: ",df_3.cumsum())

#Conocer los datos menores de cada una de las columnas
print("\nDatos menores columnas DF: ",df.min())

#Conocer los datos mayores de cada una de las columnas
print("\nDatos mayores de las columnas DF: ",df.max())

#Calcular la media aritmética de cada una de las columnas
print("\nMedia aritmétia de las columnas del DF_3: ",df_3.mean())

#calcular la desviación standard de cada una de las columnas
print("\nDesviación standard de las columnas del DF_3: ",df_3.std())

#Conocer la mediana de cada columna
print("\nMediana de cada columna: ",df.median())

#Conocer la correlación entre las columnas
print("\nCorrelación entre las columnas: ",df.corr())

#Eliminar las filas donde hallan datos nulos
#pd.dropna(axis = 1) puedo eliminas las columnas
print("\nEliminar las filas del DF con datos nulos: ",df.dropna())

#Rellenar los espacios donde hay datos nulos
#Con df.fillna(valor) podemos rellenar los espacios que contienen valores nulos
print("\nDF con espacios nulos remplazados por un valor: ",df.fillna(5))

#Con la instrucción df.isnull().sum() obtenemos la suma de datos nulos
print("\nHay datos nulos en el DF info_paises: ", info_paises.isnull())


#Eliminar columnas de un DF
#del df_csv['colesterol']
#print("\nEliminar la columna colesterol del DF csv: ",df_csv)

#print("\nEliminar la columna capital de info_paises: ",info_paises.pop('Capital') )

#Añadir una fila al DF
s_1 = pd.Series(['Colombia', 'Bogotá', 1.775, 50.34], index=['País','Capital','Area','Población'])
info_paises = info_paises.append(s_1, ignore_index=True)
print("\nInfo paises con una nueva fila: ", info_paises)
  
#Eliminar una fila de un DF
print("\nDF 3 sin la fila 4: ",df_3.drop([4]))

#Filtrar las filas de un DF
print("\nDF csv filtrado: ")
print(df_csv[df_csv['sexo']=='H'])

#Ordenar un DF
print("\nDF ordenado de manera descendente: ",df.sort_values(2, ascending=False))

#Ordenar un Df según el nombre de las filas
print("\ndata_1 ordenado de manera ascendente: ",data_1.sort_index())

#Dividir el Df por grupos
print("\nInfo_paises dividido: ",info_paises.groupby(['País','Capital']).groups)

#Filtrar el DF usando el metodo group
print("\n CSV filtrado con el método group: ")
print(df_csv.groupby(['sexo']).get_group('H'))

#Funciones de caracterización por grupos
#min, max, count, mean, sum, count_nonzero
print("\n CSV filtrado y caracterizado: ")
print(df_csv.groupby('sexo').agg(np.mean))

#df.melt(id_vars=id-columnas, value_vars=columnas, var_name=nombre-columnas, var_value=nombre-valores) 
#Devuelve el DataFrame que resulta de convertir el DataFrame df de formato ancho a formato largo.
#Todas las columnas de lista columnas se reestructuran en dos nuevas columnas con nombres 
#nombre-columnas y nombre-valores que contienen los nombres de las columnas originales y 
#sus valores, respectivamente. Las columnas en la lista id-columnas se mantienen sin 
#reestructurar. 
#Si no se pasa la lista columnas entonces se reestructuran todas las columnas excepto 
#las columnas de la lista id-columnas.

#df.pivot(index=filas, columns=columna, values=valores) : Devuelve el DataFrame que resulta 
#de convertir el DataFrame df de formato largo a formato ancho. Se crean tantas columnas nuevas 
#como valores distintos haya en la columna columna. Los nombres de estas nuevas columnas son 
#los valores de la columna columna mientras que sus valores se toman de la columna valores. 
#Los nombres del índice del nuevo DataFrame se toman de los valores de la columna filas.












    
  
































