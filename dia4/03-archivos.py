archivo = open('alumnos.txt', 'r')
contenido = archivo.read()
print(contenido)
print(type(contenido))
archivo.close()


archivo = open('alumnos.txt', 'a')
archivo.write('\n')
archivo.write('4,Maria,maria@gmail.com,23')
archivo.close()


archivo = open('alumnos.txt', 'w')
archivo.write('1,Juan,juan@gmail.com,20')
archivo.close()