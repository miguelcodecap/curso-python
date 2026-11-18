

lista_de_precios= [168.21,164.08,166.45,162.90,165.37]
cierre_de_nuevo_dia = float(input("Cierre de nuevo día: "))
lista_de_precios.append(cierre_de_nuevo_dia)
ganancia_al_dia_de_hoy = lista_de_precios[-1]-lista_de_precios[0]
rendimiento = ganancia_al_dia_de_hoy/lista_de_precios[0] *100
rango = max(lista_de_precios) - min(lista_de_precios)

#ejercicio 2:


promedio = sum(lista_de_precios)/ len(lista_de_precios)


print(f"El precio del primer día fue ${lista_de_precios[0]:.2f}")
print(f"El precio del último día fue ${lista_de_precios[-1]:.2f}")
print(f"Hay {len(lista_de_precios)} precios en la lista")
print(f"Rendimiento de la semana fue: {rendimiento:.2f}%")

#ejercicio 2:

print(f"Hay {len(lista_de_precios)} precios")
print(f"El precio más alto es de ${max(lista_de_precios):.2f}")
print(f"El precio más bajo fue de ${min(lista_de_precios):.2f}")
print(f"El promedio de los cierres es de ${promedio:.2f}")
print(f"El rango fue de ${rango:.2f}")
