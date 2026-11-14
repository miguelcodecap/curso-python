
#Ejercicio 1
accion1 = ("SCCO")  # nombre de la acción
precio1 = (34)
print ("nombre de la accion:",accion1 , "precio de la accion:",precio1)


#Ejercicio 2

precio2 = (45)   # precio de la acción
cantidad_comprada = (20)
monto_total_invertido = ( precio2 * cantidad_comprada)
print ("inversion total:",monto_total_invertido)

#Ejercicio 3

precio_actual_accion2 = (52)
variacion_porcentual = ((precio_actual_accion2/precio2)-1)
ganancia_total = ((monto_total_invertido*variacion_porcentual))
print ("ganancia total:", ganancia_total , "variación porcentual", (variacion_porcentual*100),"%")
