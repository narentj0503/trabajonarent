materias=["matematica","español","ciencias","sociales","fisica","quimica"]
#para determinar el tamañod e la lista podemos  ussar len()
print(len(materias))
print(dir(materias))

#podemos accedeer a los elementos indicanco la posisicon
print(materias[2])

#slicing muestra las posiciones en un rango
print(materias[2:5])

print(materias[3:])#para que muestre del 3 hasta el final de la lista

print(materias[:5])#para que muestre todo lo de antes de la posicion 5

print(materias[-5:-1])

print(materias[1:5])

#tipos de datos

edades=[17,34,20,67,82]

print(type(edades))#para mirar que tipo de lista es

#actualizar un elementi de la lista

materias[2]="biologia"

print(materias[0:])

materias[1:3]="Lenguaje","ciencias naturales"

print(materias[0:])
#agregando elementos  ala lista

#materias.append("Religion","Etica")

print(materias[0:])

materias.insert(0,"Etica")
print(materias[0:])

#pop elimina
materias.pop(0)
print(materias[0:])

#materias.remove(0,"Etica")
#print(materias[0:])

##del materias[4]#del borra la base de datos
#print(materias[0:])

##materias.clear()#limpiar la lista
##print(materias[0:])

#iterar las listas con el ciclo for

for i in materias:
    print(i)
    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("-"*50)#esto es para hacer varios guiones como arriba
    
for i in range(len(materias)):
        print(materias[i])
        print("-"*50)
        
for i,materias in enumerate(materias):
            print(i,materias)
            print("-"*50)
            
            #ussando en el ciclo while
            i=0
while i<len(materias):
                print(materias[i])
                i+=1
                print("-"*50)
                