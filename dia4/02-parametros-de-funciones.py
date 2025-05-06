# Args
def sumar(*args):
    resultado = 0
    for arg in args:
        resultado = resultado + arg

    return resultado

print(sumar(1, 2, 4, 7, 8))


# Kwargs
def usuario(**kwargs):
    nombre = kwargs.get('nombre')
    dni = kwargs.get('dni')
    edad = kwargs.get('edad')

    return f"Hola, me llamo {nombre}, mi dni es {dni} y tengo {edad} años"

print(usuario(nombre="Juan", dni="78787878", edad=27))