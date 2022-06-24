import mysql.connector
from contextlib import closing

conexion = mysql.connector.connect(host='localhost', database='test_db', user='root', password='')

try:
    with closing(conexion):
        with closing(conexion.cursor()) as cursor:
            sentencia = 'INSERT INTO persona(id_persona, nombre, apellido, email) VALUES(NULL,%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@mail.com')
            cursor.execute(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
