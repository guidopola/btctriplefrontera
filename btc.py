#!/usr/bin/python

import urllib.request
import json

#-------------------------------------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------") 
														#Precio BTC en GUARANIES

precioPYGYDOLAR = urllib.request.urlopen('https://py.coinmonitor.info/data_py.json') # Define variable que contiene el link del json
data1 = json.loads(precioPYGYDOLAR.read()) 	# Define variable que carga y lee el json

print("1 BTC = " + (data1["stampxdolar"] + " Guaranies | Paraguay | PYG ")) # Dentro del json devolver el valor "stampxdolar" en pantalla


#-------------------------------------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------") 
														#Precio BTC en ARS

precioARS = urllib.request.urlopen('https://coinmonitor.info/data_ar.json') # Define variable que contiene el link del json
data2 = json.loads(precioARS.read()) # Define variable que carga y lee el json con la data

print("1 BTC = " + (data2["titulo"] + " | ARS")) # Dentro del json devolver el valor "titulo" en pantalla

#-------------------------------------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------") 
														#Precio BTC en Reales

precioBRL = urllib.request.urlopen('https://br.coinmonitor.info/data_br.json') # Define variable que contiene el link del json
data3 = json.loads(precioBRL.read()) # Define variable que carga y lee el json 

print("1 BTC = " + (data3["stampxdolar"] + " Reais | Brasil | BRL ")) # Dentro del json devolver el valor "stampxdolar" en pantalla

#-------------------------------------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------")														
														#Precio BTC en USD BITSTAMP

precioUSD = urllib.request.urlopen('https://coinmonitor.info/data_ar.json') # Define variable que contiene el link del json
data4 = json.loads(precioUSD.read()) # Define variable que carga y lee el json

print("1 BTC = " + (data4["bitstamp"] + " Bitstamp | USD ")) # Dentro del json devolver el valor "bitstamp" en pantalla



print("-----------------------------------------------") 

