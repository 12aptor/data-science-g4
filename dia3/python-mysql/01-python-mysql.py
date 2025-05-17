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
    #cerramos la conexion
    connection.close()
except mysql.connector.Error as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")
    


