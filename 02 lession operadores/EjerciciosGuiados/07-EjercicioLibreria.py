print('Proporcione los siguientes datos del libro:')

NombreLibro = input("Propociona el nombre: ")
idLibro = int(input("Propocione el ID: "))
precio = float(input("Propocione el precio: "))
envioGratuito = input("Indica si el envio es gratuito (True/False): ")

if (envioGratuito == 'True'):
  envioGratuito = True
elif(envioGratuito == 'False'):
  envioGratuito = False
else:
  envioGratuito = 'Valor incorrecto, debe escribir True o False'
  
print(f'''
  Nombre: {NombreLibro}
	ID: {idLibro}
	Precio :{precio}
	El envio gratuito?: {envioGratuito}  
''')