#Pagos

#pago = input("Desea hacer el pago? ")
#if pago.lower() == "si":
    #valor_pagar = int(input("Ingrese el valor a pagar: ")) 
   # servicio = input("Desea agregar el servicio (propina)? ")
   # if servicio.lower() == "si":
    #    valor_pagar += valor_pagar * 0.10
    #print(f"El monto total a pagar es: {valor_pagar}, gracias por su visita")
#else:
    #nuevo_pedido = input("¿Desea hacer otro pedido? (si/no): ")
   # if nuevo_pedido.lower() == "si":
      #  print("Pronto seras atendid@")


#Registro e ingreso
reg = input("Deseas registrarse? ")
if reg.lower() == "si":
    name = input("Nombre: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    tel = int(input("Telefono: "))
    scaptcha = int(input("¿Cuánto es 2 + 2? "))
    if scaptcha != 4:
        print("Verificación fallida. Registro cancelado.")
    else:
        print("Registro Completo ")

        ingreso = input("Deseas ingresar con email o telefono? ")
        if ingreso.lower() == "email":
            ver = input("Ingrese el email: ")
            if ver == email:
                print("Bienvenido")
            else:
                print("Email incorrecto")
        elif ingreso.lower() == "telefono":
            vertel = input("Ingrese el telefono: ")
            if int(vertel) == tel:
                print("Bienvenido")
            else:
                print("Telefono incorrecto")





