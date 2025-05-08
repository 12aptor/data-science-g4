def crear_archivo():
    """Función para crear el archivo si no existe"""
    try:
        with open('empresas.txt', 'x') as archivo:
            archivo.write('id,nombre,email')
    except FileExistsError:
        pass

def mostrar_titulo(titulo):
    """Función para mostrar el título"""
    print(f"""
    ==============================
        {titulo}
    ==============================

    """)

def pedir_datos_empresa():
    """Función para pedir los datos de una empresa"""
    nombre = input('Nombre de la empresa: ')
    email = input('Email de la empresa: ')
    return nombre, email

def crear_empresa():
    """Función para crear una empresa"""
    mostrar_titulo('Registrar una empresa')
    nombre, email = pedir_datos_empresa()

    crear_archivo()

    with open('empresas.txt', 'a') as archivo:
        archivo.write('\n')
        archivo.write(f'1,{nombre},{email}')

def listar_empresas():
    """Función para listar las empresas"""
    mostrar_titulo('Listar empresas')
    try:
        with open('empresas.txt', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas[1:]:
                datos = linea.strip().split(',')
                id_empresa = datos[0]
                nombre_empresa = datos[1]
                email_empresa = datos[2]
                print(f"ID: {id_empresa}, Nombre: {nombre_empresa} Email: {email_empresa}")

    except FileNotFoundError:
        print('No hay empresas registradas.')

def actualizar_empresa():
    """Función para actualizar una empresa"""
    mostrar_titulo('Actualizar una empresa')
    listar_empresas()
    id_empresa_recibido = input('\nID de la empresa a actualizar: ')

    lineas_actualizadas = []
    encontrado = False

    with open('empresas.txt', 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            datos = linea.strip().split(',')
            id_empresa = datos[0]

            if id_empresa == id_empresa_recibido:
                encontrado = True
                nombre, email = pedir_datos_empresa()
                linea_actualizada = f'{id_empresa},{nombre},{email}\n'
                lineas_actualizadas.append(linea_actualizada)
            else:
                lineas_actualizadas.append(linea)

    if not encontrado:
        print('\nNo se encontró la empresa con ese ID.')
        return
    
    with open('empresas.txt', 'w') as archivo:
        archivo.write('id,nombre,email\n')
        archivo.writelines(lineas_actualizadas)