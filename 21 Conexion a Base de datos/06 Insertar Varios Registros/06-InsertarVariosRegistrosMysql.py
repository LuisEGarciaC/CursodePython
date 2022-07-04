import mysql.connector
from contextlib import closing

conexion = mysql.connector.connect(host='localhost', database='test_db', user='root', password='')

try:
    with closing(conexion):
        with closing(conexion.cursor()) as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('Marcos', 'Cantu', 'mcantu@mail.com'),
                ('Angel', 'Quintana', 'aquintana@mail.com'),
                ('Maria', 'Gonzalez', 'mgonzalez@mail.com')
            )
            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
