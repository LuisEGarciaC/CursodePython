import mysql.connector
from contextlib import closing

conexion = mysql.connector.connect(host='localhost',
                                         database='test_db',
                                         user='root',
                                         password='')

try:
    with closing(conexion):
      with closing(conexion.cursor()) as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Proporciona el valor id_pesona: ')
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()