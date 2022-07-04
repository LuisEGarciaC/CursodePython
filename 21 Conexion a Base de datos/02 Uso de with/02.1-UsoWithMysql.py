import mysql.connector
from mysql.connector import Error
from contextlib import closing
# importamos closing para cerra los with

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='test_db',
                                         user='root',
                                         password='')
    
    with closing(connection):
      with closing(connection.cursor()) as cursor:
        cursor = connection.cursor()
        sentencia = 'SELECT * FROM persona'
        cursor.execute(sentencia)
        registros = cursor.fetchall()
        print(registros)
        cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is cerrada")
