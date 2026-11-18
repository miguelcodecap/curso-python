

ticker = input("ticker: ")
monto_disponible = float(input("monto disponible: "))
precio_por_accion = float(input("precio por acción: "))

#cálculos:

cuantas_acciones_puedo_comprar= int(monto_disponible/precio_por_accion)
costo_de_acciones= cuantas_acciones_puedo_comprar*precio_por_accion
cuanto_dinero_sobra= monto_disponible-costo_de_acciones

print(f"---Acciones de {ticker}---")
print(f"Puedo comprar {cuantas_acciones_puedo_comprar} acciones")
print(f"La compra de las acciones tiene un valor de ${costo_de_acciones:.2f}")
print(f"Sobra ${cuanto_dinero_sobra:.2f}")
