dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

""" Recuperar elementos de la lista """
# print(dias)
# print(dias[3])
# print(dias[-2])
# print(dias[1:3])

""" Agregar elementos a la lista """
dias.append("Sábado")
dias.append("Domingo")

""" Eliminar elementos de la lista """
dias.pop(2)
del dias[0]

""" Actualizar elementos de la lista """
dias[-1] = "DOMINGO"

""" Recorrer la lista """
for dia in dias:
    print(dia)