from empresas.lib_empresas import (
    crear_empresa,
    listar_empresas,
    actualizar_empresa,
)
import os

while True:
    print("""
    ==============================
        Administrador de Empresas
    ==============================
        1. Registrar una empresa
        2. Listar las empresas
        3. Actualizar una empresa
        4. Eliminar una empresa
        5. Salir
    """)
    opcion = int(input('Elegir una opción: '))

    os.system('clear')

    if opcion == 1:
        crear_empresa()
    elif opcion == 2:
        listar_empresas()
    elif opcion == 3:
        actualizar_empresa()
    break