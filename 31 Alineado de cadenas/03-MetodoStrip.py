# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:', titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:', titulo)
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:', titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:', titulo)

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada:', titulo)
