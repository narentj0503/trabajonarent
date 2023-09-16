import random

captchas = [
    {"pregunta": "5 + 3", "respuesta": 8},
    {"pregunta": "9 - 4", "respuesta": 5},
    {"pregunta": "2 * 6", "respuesta": 12}
    # Agrega más preguntas y respuestas si lo deseas
]


def calcular_historial_compra():
    valor_compra = float(input("Ingrese el valor total de la compra: "))
    cuotas = int(input("Ingrese la cantidad de cuotas deseadas: "))
    saldo_pendiente = valor_compra
    cuota = valor_compra / cuotas
    cupofa = 0
    mes = 1
    
    while mes <= cuotas:
        print(f"Mes {mes}:")
        print(f"Cuota a pagar: ${cuota:.2f}")
        print(f"Saldo pendiente: ${saldo_pendiente:.2f}")
        print(f"Cupo a favor: ${cupofa:.2f}")
        
        saldo_pendiente -= cuota
        cupofa += cuota
        mes += 1

while True:
    opcion = input("¿Qué deseas realizar? 1=Registro, 2=Login, 3=Salir: ")
    
    if opcion == "1":
        name = input("Nombre: ")
        email = input("Email: ")
        password = input("Contraseña: ")
        tel = int(input("Telefono: "))
        
        captcha = random.choice(captchas)
        pregunta_captcha = captcha["pregunta"]
        respuesta_captcha = captcha["respuesta"]
        
        scaptcha = int(input(f"¿Cuánto es {pregunta_captcha}? "))
        if scaptcha != respuesta_captcha:
            print("Verificación fallida. Registro cancelado.")
        else:
            print("Registro Completo")
    
    
    elif opcion == "2":
        while True:
            ingreso = input("¿Deseas ingresar con email o telefono? ")
            
            if ingreso.lower() == "email":
                ver_email = input("Ingrese el email: ")
                ver_password = input("Ingrese la contraseña: ")
                
                if ver_email == email and ver_password == password:
                    print("Bienvenido")
                    while True:
                        op = input("¿A dónde quieres ir? 1=historial de compra, 2=juego, 3=volver: ")
                        if op == "1":
                            calcular_historial_compra()
                        elif op == "2":
                            vidas = 5
                            puntos = 0
                            
                            while vidas != 0:
                                num = random.randint(0, 9)
                                
                                if num == 0:
                                    vidas -= 1
                                    print(f"Te quedan {vidas} vidas")
                                else:
                                    puntos += 1
                                    print(f"Has ganado {puntos} puntos")
                        elif op == "3":
                            print("Volviendo al menú anterior...")
                            break
                        else:
                            print("Opción inválida")
                    break  # Salir del bucle interno si las credenciales son correctas
                else:
                    print("Credenciales incorrectas. Intenta de nuevo.")
                    
            elif ingreso.lower() == "telefono":
                ver_tel = input("Ingrese el teléfono: ")
                ver_password = input("Ingrese la contraseña: ")
                
                if int(ver_tel) == tel and ver_password == password:
                    print("Bienvenido")
                    while True:
                        op = input("¿A dónde quieres ir? 1=historial de compra, 2=juego, 3=volver: ")
                        if op == "1":
                            calcular_historial_compra()
                        elif op == "2":
                            vidas = 5
                            puntos = 0
                            
                            while vidas != 0:
                                num = random.randint(0, 9)
                                
                                if num == 0:
                                    vidas -= 1
                                    print(f"Te quedan {vidas} vidas")
                                else:
                                    puntos += 1
                                    print(f"Has ganado {puntos} puntos")
                        elif op == "3":
                            print("Volviendo al menú anterior...")
                            break
                        else:
                            print("Opción inválida")
                    break  # Salir del bucle interno si las credenciales son correctas
                else:
                    print("Credenciales incorrectas. Intenta de nuevo.")
                    
            else:
                print("Opción inválida")
    
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")