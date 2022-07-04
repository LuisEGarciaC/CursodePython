from logger_base import log
import mysql.connector
# from mysql.connector import Error
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'root'
    _PASSWORD = ''
    _DB_PORT = '3306'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = mysql.connector.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener la conexión Exception: {e}')
                sys.exit()
        else:
          return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener el cursor Exception: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()

