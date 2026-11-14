#Ejercicio 1: Calcular el valor total de una inversión en acciones.

cantidad_de_acciones = 15
precio_de_accion0 = 80
valor_total = cantidad_de_acciones * precio_de_accion0
print("Valor total de la inversión:", "$" , valor_total)


#Ejercicio 2: Portafolio de acciones.
empresa = "SCCO"
cantidad_de_acciones = 10
precio_de_accion = 95
monto_invertido = cantidad_de_acciones * precio_de_accion


empresa2 = "Empresa2"
cantidad_de_acciones2 = 25
precio_de_accion2 = 40
monto_invertido2 = cantidad_de_acciones2 * precio_de_accion2


monto_invertido_total = monto_invertido + monto_invertido2
porcentaje_en_portafolio_empresa1 = monto_invertido / monto_invertido_total*100
porcentaje_en_portafolio_empresa2 = monto_invertido2 / monto_invertido_total*100

print("Monto invertido en", empresa , ": $", monto_invertido)
print("Monto invertido en", empresa2 ,": $", monto_invertido2)
print("Monto total del portafolio: $", monto_invertido_total)
print("Porcentaje de", empresa, "en portafolio:", porcentaje_en_portafolio_empresa1,"%")
print("Porcentaje de", empresa2, "en portafolio:",porcentaje_en_portafolio_empresa2,"%")


#Ejercicio interés compuesto

capital_inicial = 5000
tasa_de_interés = 0.06   #anual
plazo = 5 #años

valor_futuro = (capital_inicial*((1+tasa_de_interés)**plazo))
interés_ganado = valor_futuro - capital_inicial

print("Valor futuro:$",valor_futuro)
print("Interés ganado:$", interés_ganado)
