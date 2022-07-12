from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log


class UsuarioDAO:
    '''
                        DAO (Data Access Object) para la tabla usuario
                        CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug(f'Seleccionando usuarios...')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2],)
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar un registro
    # usuario1 = Usuario(username='hades8', password='Darkaldebaran')
    # usuarios_insertados = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuarios insertados: {usuarios_insertados}')

    # Actualizar un registro
    # usuario1 = Usuario(2, 'songoku', 'SSJ3Vegeta')
    # usuarios_modifiacar = UsuarioDAO.actualizar(usuario1)
    # log.debug(f'Personas actualizadas: {usuarios_modifiacar}')

    # Eliminar un registro
    # usuario1 = Usuario(id_usuario=7)
    # usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Personas eliminadas: {usuarios_eliminados}')

    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
