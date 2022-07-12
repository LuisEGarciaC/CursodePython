import logging as log
import pathlib

# Obtengo la ruta absoluta
path = pathlib .Path( __file__ ) .parent .absolute()


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler(str( path ) +'/capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel DEBUG')
    log.info('Mensaje a nivel INFO')
    log.warning('Mensaje a nivel de WARNING')
    log.error('Mensaje a nivel de ERROR')
    log.critical('Mensaje a nivel CRITICO')
