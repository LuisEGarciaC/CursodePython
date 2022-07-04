# importamos el modulo
import psycopg2 
 

#En primer lugar, crear un objeto conexión.
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# Posteriormente, crear un objeto de tipo cursor.
cursor = conexion.cursor()
# Definir la sentencia que queremos ejecutar.
sentencia = 'SELECT * FROM persona'
# Mandar a llamar el método execute con ayuda del objeto cursor y con este objeto cursor podemos solicitar
cursor.execute(sentencia)
# llamamos todos los registros todos los registros.
# Resultados de ejecutar la sentencia que hemos proporcionado, en este caso con el método Fetch Hold
registros = cursor.fetchall()
# Por último, lo mandamos a imprimir y observamos una lista con todos estos registros y como último paso
print(registros)

#cerramos el objeto cursor y el objeto conexión.
cursor.close()
conexion.close()