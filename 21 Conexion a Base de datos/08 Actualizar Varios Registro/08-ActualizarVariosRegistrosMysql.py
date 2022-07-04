import mysql.connector
from contextlib import closing

conexion = mysql.connector.connect(host='localhost', database='test_db', user='root', password='')

try:
    with closing(conexion):
        with closing(conexion.cursor()) as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan', 'Perez', 'jperez@mail.com', 1),
                ('Ivonne', 'Gutierrez', 'igutierrez@mail.com', 2)
            )
            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
