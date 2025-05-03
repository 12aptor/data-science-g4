usuario = {
    "id": 1,
    "nombre": "Juan",
    "edad": 20,
    "direccion": {
        "calle": "Avenida los girasoles",
        "numero": 123,
        "piso": 1,
        "coordenadas": (1.23, 4.56),
    },
    "telefono": "123456789",
}

""" Recuperar elementos de un diccionario """
print(usuario["nombre"])
print(usuario["direccion"]["coordenadas"])

""" Agregar elementos a un diccionario """
usuario["correo"] = "juan@gmail.com"

""" Eliminar elementos de un diccionario """
usuario.pop("edad")
del usuario["direccion"]

""" Recorrer un diccionario """
for key, value in usuario.items():
    print(f"{key}: {value}")

for key in usuario:
    print(key, usuario[key])

for key in usuario.keys():
    print(key, usuario[key])

for value in usuario.values():
    print(value)