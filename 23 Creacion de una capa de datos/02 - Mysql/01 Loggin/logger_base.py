import logging as log

log.basicConfig(level=log.DEBUG)

# SE PUEDE CAMBIAR DEBUG A OTRO ESTADO Y ESA ES LA INFORMACION QUE APARECERA EN CONSOLA

if __name__ == '__main__':
  log.debug('Mensaje a nivel debug')
  log.info('Mensaje a nivel info')
  log.warning('Mensaje a nivel de warning')
  log.error('Mensaje a nivel de error')
  log.critical('Mensaje a nivel critico')
