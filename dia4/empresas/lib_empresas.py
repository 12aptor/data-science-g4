def crear_archivo():
    """Función para crear el archivo si no existe"""
    try:
        with open('empresas.txt', 'x') as archivo:
            archivo.write('id,nombre,email')
    except FileExistsError:
        pass

def pedir_datos_empresa():
    """Función para pedir los datos de una empresa"""
    nombre = input('Nombre de la empresa: ')
    email = input('Email de la empresa: ')
    return nombre, email

def crear_empresa():
    """Función para crear una empresa"""
    nombre, email = pedir_datos_empresa()

    crear_archivo()

    with open('empresas.txt', 'a') as archivo:
        archivo.write('\n')
        archivo.write(f'1,{nombre},{email}')