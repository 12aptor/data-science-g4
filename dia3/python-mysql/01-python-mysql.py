import mysql.connector

try:
    #creamos una conexión a la bd
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_g4'
    )
    print(f'estas conectado a la base de datos : {connection.database}')
    
    # insertamos datos en la base de datos
    #alumno_cursor = connection.cursor()
    #alumno_cursor.execute("insert into alumno(nombre,email) values('cesar mayta','cesar@gmail.com');")
    #connection.commit()
    #print('alumno insertado')
    
    # seleccionar los alumnos
    alumno_select_cursor = connection.cursor()
    alumno_select_cursor.execute("select nombre,email from alumno")
    resultado = alumno_select_cursor.fetchall()
    for fila in resultado:
        print('*'*50)
        print(f'NOMBRE : {fila[0]}')
        print(f'EMAIL : {fila[1]}')
    #cerramos la conexion
    connection.close()
except mysql.connector.Error as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")
    


