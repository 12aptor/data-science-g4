while True:
    print("MINI CALCULADORA")
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))
    operacion = input("¿Qué operación desea realizar? (SUMA, RESTA, MULTIPLICACION, DIVISION): ")

    if operacion == "SUMA":
        resultado = numero_1 + numero_2
    elif operacion == "RESTA":
        resultado = numero_1 - numero_2
    elif operacion == "MULTIPLICACION":
        resultado = numero_1 * numero_2
    elif operacion == "DIVISION":
        resultado = numero_1 / numero_2
    else:
        print("Operación incorrecta")
        continue

    print(f"El resultado es: {resultado}")