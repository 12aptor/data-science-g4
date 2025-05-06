from empresas.lib_empresas import crear_empresa

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

    if opcion == 1:
        crear_empresa()
