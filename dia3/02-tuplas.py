""" Las tuplas son listas que no pueden mutar """
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")


""" Agregar elementos a la lista """
dias = list(dias)
dias.append("Sábado")
dias = tuple(dias)

for dia in dias:
    print(dia)