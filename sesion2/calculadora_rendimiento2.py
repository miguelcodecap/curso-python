

ticker = input("ticker: ")
cantidad_de_acciones = int(input("cantidad de acciones "))
precio_por_accion = float(input("precio por accion "))
dividendo_anual_por_accion = float(input("dividendo anual por accion "))

inversion_total = round( cantidad_de_acciones * precio_por_accion , 2)
ingreso_anual_por_dividendos = round(dividendo_anual_por_accion * cantidad_de_acciones, 2)
rendimiento_por_dividendo = round((dividendo_anual_por_accion / precio_por_accion)* 100, 2)
años_para_recuperar_inversion_con_dividendos= round(inversion_total / ingreso_anual_por_dividendos,2)


print("Inversión total de " , inversion_total)
print("Ingreso anual por dividendo " , ingreso_anual_por_dividendos)
print("Rendimiento por dividendo " , rendimiento_por_dividendo ,"%")
print("años para recuperar inversión" , años_para_recuperar_inversion_con_dividendos)  