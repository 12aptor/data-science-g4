edad = 15

if edad >= 18:
    print("Eres mayor de edad")


# ###########################
print("MINI CALCULADORA")

numero_1 = input("Ingrese el primer número: ")
numero_2 = input("Ingrese el segundo número: ")
operacion = input("¿Qué operación desea realizar? (SUMA, RESTA, MULTIPLICACION, DIVISION): ")

if operacion == "SUMA":
    resultado = int(numero_1) + int(numero_2)
elif operacion == "RESTA":
    resultado = int(numero_1) - int(numero_2)
elif operacion == "MULTIPLICACION":
    resultado = int(numero_1) * int(numero_2)
elif operacion == "DIVISION":
    resultado = int(numero_1) / int(numero_2)
else:
    print("Operación incorrecta")
    exit()

print(f"El resultado es: {resultado}")