Ejrecicoplidoras
print("============================")
print("  ¡Bienvenido(a) Saludos!  ")
print("============================")
print("Se te pedira 2 números los cual el primer numero sera el número a multiplicar * 2 y el segundo la cantidad de veces que se realizara .")


# comenzamos

numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))

def operacion(a, b):
 
	valor_de_a = a
    
	array = [a]
    
	inicial = 0
    
	while inicial <= b :
        
		agregar = valor_de_a * 2
        
		array.append(agregar)
        
		valor_de_a = agregar
        
		inicial += 1 
    
	else:
        
		print("el resultado es:", array)
    


operacion(numero1, numero2)
