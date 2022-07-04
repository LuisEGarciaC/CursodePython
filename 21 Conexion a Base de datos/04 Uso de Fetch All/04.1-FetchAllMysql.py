import mysql.connector
from contextlib import closing
from mysql.connector import Error

conexion = mysql.connector.connect(host='localhost', database='test_db', user='root', password='')

try:
    with closing(conexion):
      with closing(conexion.cursor()) as cursor:
        # sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
        # llaves_primarias = ((1,2,3,4),)
        # llaves_primarias1 = ((1,2,3,4,),)
        # llaves_primarias2 = (1,2,3,4,5,6,7,8,)
        entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
        llaves_primarias = tuple(entrada.split(','))
        for row in llaves_primarias:
          # print(row)
          cursor.execute(f'SELECT * FROM persona WHERE id_persona = {row}')
          registros = cursor.fetchall()
          if registros != []:
            print(registros)
          else:
            print(f"Los resgistros buscados por la id {row} no existen")

except Error as e:
    print("Error ", e)
finally:
    conexion.close()
    
    
#NOTA
'''
ya que no me funciono la forma parecida a 
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

decidi recorrer la informacion y por cada recorrido ejecuto la sentencia
cuando logre resolver actualizare
'''