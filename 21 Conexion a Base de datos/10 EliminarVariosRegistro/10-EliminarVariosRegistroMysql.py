import mysql.connector
from contextlib import closing

conexion = mysql.connector.connect(host='localhost', database='test_db', user='root', password='')

try:
    with closing(conexion):
        with closing(conexion.cursor()) as cursor:
            sentencia = """DELETE FROM persona WHERE id_persona = %s"""
            # entrada = input('Proporciona los id_persona a eliminar (separados por coma): ')
            # valores = tuple(entrada.split(','))
            prueba = [(12,),]
            print(prueba)
            prueba = cursor.executemany(sentencia,prueba)
            conexion.commit()
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
