
def calcular_historial_compra():
    valor_compra = float(input("Ingrese el valor total de la compra: "))
    cuotas = int(input("Ingrese la cantidad de cuotas deseadas: "))
    saldo_pendiente = valor_compra
    cuota = valor_compra / cuotas
    cupofa = 0
    mes = 1
    
    while mes <= cuotas:
        print(f"Mes {mes}:")
        print(f"Cuota a pagar: ${cuota:}")
        print(f"Saldo pendiente: ${saldo_pendiente:}")
        print(f"Cupo a favor: ${cupofa:}")
        
        saldo_pendiente -= cuota
        cupofa += cuota
        mes += 1

calcular_historial_compra()
    