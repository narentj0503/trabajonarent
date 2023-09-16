
    
entradas=int(input("cuantas entradas de dinero tiene usted?: "))

entra=[]

for i in range (entradas):
    entraa = input(f"ingrese el nombre de la entrada y su valor {i + 1}: ")
    
    entra.append(entraa)


print(":", entra)

    
cantgastosfijos = int(input("cuantos gastos fijos tiene mensualmente?: "))

gastosfijos = []

for i in range(cantgastosfijos):
 
    gastof = input(f"ingrese el nombre del gasto y su valor {i + 1}: ")
    
    gastosfijos.append(gastof)


print(":", gastosfijos)


