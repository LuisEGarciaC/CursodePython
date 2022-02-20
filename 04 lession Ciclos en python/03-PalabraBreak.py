palabra = 'Holanda'
for letra in palabra:
  print(f'la letra encontrada es {letra}')
  if letra == 'a':
      print(f'Letra encontrada: {letra}')
      break
else:
    print('Fin ciclo for')
