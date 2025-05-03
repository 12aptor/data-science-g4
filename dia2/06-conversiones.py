# Programa para convertir divisas de soles dolares y viceversa
import os
import time

condicion = True
while condicion:
    print("""
        ==========================
          CONVERSIONES DE DIVISAS
        ==========================
          [1] Convertir soles a dolares
          [2] Convertir dolares a soles
          [3] Salir
        ==========================
    """)
    opcion = int(input("Elija una opción: "))
    os.system("clear")
    os.system("cls")
    if opcion == 1:
        print("""
            ==========================
              CONVERTIR SOLES A DOLARES
            ==========================
        """)
        soles = float(input("Ingrese el monto en soles: "))
        dolares = round(soles / 3.67, 2)
        print(f"El monto el dolares es: {dolares}")

    elif opcion == 2:
        print("""
            ==========================
              CONVERTIR DOLARES A SOLES
            ==========================
        """)
        dolares = float(input("Ingrese el monto en dolares: "))
        soles = round(dolares * 3.67, 2)
        print("El monto en soles es:", soles)
    elif opcion == 3:
        print("Saliendo del programa...")
        condicion = False
    else:
        print("Opción incorrecta")

    time.sleep(2)
    os.system("clear")
    os.system("cls")