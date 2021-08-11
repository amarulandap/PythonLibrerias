# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:24:22 2021

@author: Andres Marulanda
"""

"""RETO_5_VARIANTE_3"""

import pandas as pd
import csv

def Concepto(lista_read):
    
    lista_concepto = [['Fecha', 'Concepto']]
    
    for j in lista_read[1:]:
    
        if float(j[4]) < 1624:
            concepto = 'MUY BAJO'
        
        elif (float(j[4])) >= 1624 and (float(j[4])) < 1854:
            concepto =  'BAJO'
    
        elif (float(j[4])) >= 1854 and (float(j[4])) < 2084:
            concepto = 'MEDIO'
        
        elif (float(j[4])) >= 2084 and (float(j[4])) < 2314:
            concepto = 'ALTO'
        
        else:
            concepto = 'MUY ALTO'
  
        lista_concepto.append([j[0], concepto])
        
    with open('analisis_archivo.csv', 'w', newline='')as google:
        writer = csv.writer(google, delimiter = '\t')
        
        for k in lista_concepto:
            writer.writerow(k)
            

def Max_min(goog):

    lowest_mean = 0.0
    highest_mean = 0.0
    row_date_max = 0
    row_date_min = 0
    date_highest_mean = ""
    date_lowest_mean = ""

    #Copia del DF para calcular los promedios de los valores
    goog_1 = goog[['Date', 'High', 'Low']].copy()

    #Calcular los promedios de cada fila y los anexarlos al final
    goog_1['Prom'] = goog_1.mean(axis=1)

    #Hallar los promedios mas bajo y alto durante el periodo
    lowest_mean = goog_1['Prom'].min() 
    highest_mean = goog_1['Prom'].max()

    #Hallar las fechas de los promedios mas bajo y alto del periodo
    row_date_min = goog_1['Prom'].idxmin()
    row_date_max = goog_1['Prom'].idxmax()
    
    date_lowest_mean = goog_1.iloc[row_date_min, 0]
    date_highest_mean = goog_1.iloc[row_date_max, 0]
    
    return date_lowest_mean, lowest_mean, date_highest_mean, highest_mean
   


"""Programa Principal"""

lowest_mean = 0.0
highest_mean = 0.0
date_lowest_mean = ""
date_highest_mean = ""
lista_read = []
    
#leer el csv para generar una lista
with open('GOOG.csv', newline = '') as google:
    reader = csv.reader(google)
    for i in reader:
       lista_read.append(i)
       
Concepto(lista_read)

#Acceder al archivo CSV y leerlo como DF
goog = pd.read_csv('GOOG.csv', header = 0)

date_lowest_mean, lowest_mean, date_highest_mean, highest_mean = Max_min(goog)

































                





    
        

             
       

    