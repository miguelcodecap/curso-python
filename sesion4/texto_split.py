

tickers = input("Dime tickers ")
tickers_lista = tickers.split()
cantidad_de_tickers = len(tickers_lista)
primer_ticker = tickers_lista[0]
ultimo_ticker = tickers_lista[-1]
tipo_de_dato_de_lista = type(tickers_lista)
tipo_de_dato_de_datooriginal = type(tickers)

print(f"{tickers_lista}")
print(f"La cantidad de tickers es de {cantidad_de_tickers}")
print(f"El primer ticker es {primer_ticker} y el ultimo ticker es {ultimo_ticker}")
print(f"El tipo de datos de la lista es {tipo_de_dato_de_lista} y el del dato original {tipo_de_dato_de_datooriginal}")


# Ejercicio 2 - Separadores específicos

linea_de_registro_de_acceso = input("Linea de registro de acceso ")
linea_de_registro_de_acceso_campos = linea_de_registro_de_acceso.split("|")
cantidad_de_campos = len(linea_de_registro_de_acceso_campos)

print(f"La lista es {linea_de_registro_de_acceso_campos}")
print(f"La cantidad de campos es de {cantidad_de_campos}")
print(f"")
