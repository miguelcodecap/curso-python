

ticker = "   bvn  "
ticker = ticker.strip().upper()
linea_log = "  ACCESO FALLIDO user=jperez  \n"
linea_log = linea_log.strip()


print(f"El ticker es [{ticker}]")
print(f"La linea log es [{linea_log}]")
print("-------------------")
print("Ejercicio 2")

ticker2 = input("¿Cuál es el ticker? ").strip().upper()
correo = input("¿Cuál es el correo? ").strip().lower()

print(f"El ticker es [{ticker2}]")
print(f"El correo es [{correo}]")
print("-------------------")
print("Ejercicio 3")

precio_texto = "$$$165.40$$"
precio_texto = precio_texto.strip("$")
precio = float(precio_texto)
cantidad_de_acciones = 25
compra = precio * cantidad_de_acciones

print(f"El precio de la acción es ${precio:.2f}")
print(f"El valor total por las {cantidad_de_acciones} acciones es de ${compra:.2f}")

                                 