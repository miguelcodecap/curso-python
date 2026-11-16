ticker = input("Ticker ")
cantidad = int(input("cantidad de acciones "))
precio_de_compra = float(input("precio de compra "))
precio_actual = float(input("precio actual "))

inversion_inicial = cantidad * precio_de_compra
valor_actual = cantidad * precio_actual
ganancia_o_perdida = valor_actual - inversion_inicial
rendimiento = round(((ganancia_o_perdida) / (inversion_inicial) *100), 2)

print("Inversión incial de " , inversion_inicial)
print("Ganancia o pérdida de ", ganancia_o_perdida)
print("Rendimiento de ", rendimiento)