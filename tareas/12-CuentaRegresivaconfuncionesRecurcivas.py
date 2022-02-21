# Tarea: Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas

# def Restarecursiva(numero):
#   if numero < 0:
#     print('')
#   elif numero == 0:
#     return numero
#   else:
#     print(numero)
#     return numero - Restarecursiva(numero-1)


# Restarecursiva(5)


# resultado del profersor
def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero-1)

imprimir_numero_recursivo(0)