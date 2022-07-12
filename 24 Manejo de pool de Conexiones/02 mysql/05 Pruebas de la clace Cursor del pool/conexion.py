from logger_base import log
import mysql.connector.pooling as pooling
from mysql.connector import Error
import sys


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'root'
    _PASSWORD = ''
    _DB_PORT = '3306'
    _HOST = 'localhost'
    _POOLNAME = 'mysqlpool'
    _POOLSIZE = 3
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(pool_name=cls._POOLNAME,
                                                        pool_size=cls._POOLSIZE,
                                                        pool_reset_session=True,
                                                        host=cls._HOST,
                                                        user=cls._USERNAME,
                                                        password=cls._PASSWORD,
                                                        port=cls._DB_PORT,
                                                        database=cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Error as e:
                log.error(f'Ocurrió un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().get_connection()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        conexion.close()
        return conexion

    @classmethod
    def cerrarConexiones(cls):
        pool = cls.connection_object.close()
        return pool


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
