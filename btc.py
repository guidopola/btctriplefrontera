#!/usr/bin/python3
import sys
import urllib.request
import json


# Convierte el numero a float.
def convert_number(str_number):
  result = str_number
  # 24,340,003 -> 24.340.003 -> 24340.003
  return float(result.replace(',', '.').replace('.', '', 1))


def print_data(btc = 1.0):
  print("-----------------------------------------------") 
  #Precio BTC en GUARANIES

  precioPYGYDOLAR = urllib.request.urlopen('https://py.coinmonitor.info/data_py.json') # Define variable que contiene el link del json
  data1 = json.loads(precioPYGYDOLAR.read()) 	# Define variable que carga y lee el json

  value = '{:,.3f}'.format(convert_number(data1["stampxdolar"]) * btc).replace(',','.')

  print("{:.6f} BTC = {} Guaranies | Paraguay | PYG".format(btc, value))
  print("-----------------------------------------------") 
  #Precio BTC en ARS
  precioARS = urllib.request.urlopen('https://coinmonitor.info/data_ar.json') # Define variable que contiene el link del json
  data2 = json.loads(precioARS.read()) # Define variable que carga y lee el json con la data

  value = '{:,.3f}'.format(convert_number(data2["titulo_2_tt"]) * btc).replace('.', ',').replace(',', '.', 1)
  print("{:.6f} BTC = {} Pesos Argentinos | ARS".format(btc, value)) # Dentro del json devolver el valor "titulo" en pantalla
  print("-----------------------------------------------") 
  #Precio BTC en Reales

  precioBRL = urllib.request.urlopen('https://br.coinmonitor.info/data_br.json') # Define variable que contiene el link del json
  data3 = json.loads(precioBRL.read()) # Define variable que carga y lee el json 

  value = '{:,.3f}'.format(convert_number(data3["stampxdolar"]) * btc).replace('.', ',').replace(',', '.', 1)
  print("{:.6f} BTC = {} Reais | Brasil | BRL".format(btc, value)) # Dentro del json devolver el valor "stampxdolar" en pantalla
  print("-----------------------------------------------")														
  #Precio BTC en USD BITSTAMP

  precioUSD = urllib.request.urlopen('https://coinmonitor.info/data_ar.json') # Define variable que contiene el link del json
  data4 = json.loads(precioUSD.read()) # Define variable que carga y lee el json

  value = '{:,.3f}'.format(convert_number(data4["bitstamp"]) * btc).replace('.', ',').replace(',', '.', 1)
  print("{:.6f} BTC = {} Bitstamp | USD".format(btc, value)) # Dentro del json devolver el valor "bitstamp" en pantalla
  print("-----------------------------------------------") 


def main(argv):
  btc = 1.0
  if len(argv) == 2:
    print_data(float(argv[1]))
  else:
    print_data()


if __name__ == "__main__":
  main(sys.argv)
