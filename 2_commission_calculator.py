#El programa debe calcular el 15% sobre el total de las ventas realizadas para deducir las comisiones a pagar

total_ventas = float(input("Ingrese el valor total de ventas que ha realizado este mes: "))
comision = total_ventas * 0.15

print(f"Usted debe cobrar ${comision} de comisión.")