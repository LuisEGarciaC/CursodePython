from logger_base import log
import mysql.connector
from mysql.connector import pooling
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
                cls._pool = mysql.connector.pooling.MySQLConnectionPool(pool_name=cls._POOLNAME,
                                                                        pool_size=cls._POOLSIZE,
                                                                        pool_reset_session=True,
                                                                        host=cls._HOST,
                                                                        user=cls._USERNAME,
                                                                        password=cls._PASSWORD,
                                                                        port=cls._DB_PORT,
                                                                        database=cls._DATABASE)
                cls._pool.get_connection()
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Error as e:
                log.error(f'Ocurrió un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool

if __name__ == '__main__':
	Conexion.obtenerPool()
