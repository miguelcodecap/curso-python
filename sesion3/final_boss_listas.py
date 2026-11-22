

ticker = input("Ticker de acción es: ")
lista_de_precios = [158.40, 160.25, 157.90, 161.30, 163.75, 162.10, 165.40, 164.20, 166.85, 168.30]
rendimiento_del_periodo = ((lista_de_precios[-1]-lista_de_precios[0]) / lista_de_precios[0]) *100
precio_maximo = max(lista_de_precios)
precio_minimo = min(lista_de_precios)
rango = max(lista_de_precios) - min(lista_de_precios)
promedio_10_dias = sum(lista_de_precios) / len(lista_de_precios)
promedio_3_dias = sum(lista_de_precios[-3:]) / len(lista_de_precios[-3:])
diferencia_de_promedios = promedio_3_dias - promedio_10_dias







print(f"El ticker de la acción es: {ticker.upper()}")
print(f"El rendimiento del periodo es: {rendimiento_del_periodo:.2f}%")
print(f"El precio máximo es de ${precio_maximo:.2f} y el mínimo es ${precio_minimo:.2f}")
print(f"El rango es de ${rango:.2f}")
print(f"El promedio de los 10 días es de ${promedio_10_dias:.2f}")
print(f"El promedio de 3 días es de ${promedio_3_dias:.2f}")
print(f"La diferencia entre el promedio de 3 y 10 días es de ${diferencia_de_promedios:.2f}")

                