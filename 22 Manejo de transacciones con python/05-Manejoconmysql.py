import mysql.connector
from mysql.connector import Error
from contextlib import closing

conexion = mysql.connector.connect(host='localhost', database='test_db', user='root', password='')

try:
	with closing(conexion):
		with closing(conexion.cursor()) as cursor:
			sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
			valores = ('Alex', 'Rojas', 'arojas@mail.com')
			cursor.execute(sentencia, valores)

			sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
			valores = ('Juan', 'Juarez','jperez@mail.com', 1)
			cursor.execute(sentencia, valores)
			conexion.commit()
except Error as e:
	print(f'Ocurrió un error, se hizo rollback: {e}')
finally:
    conexion.close()

print('Se hizo commit...')
