"""
Proyecto Básico de Python (Piedra, Papel o Tijera).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
Versión en Español con Modificaciones: Estefania Cassingena Navone (@EstefaniaCassN).
"""
from pickle import FALSE
import random


def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    pi = ""
    pa = ""
    opcion =""
    
    if computadora == pi:
      opcion = "piedra"
    elif computadora == pa:
      opcion = "papel"
    else:
      opcion = "tijera"
      
    if usuario == computadora:
        return '¡Empate!'

    if ganó_el_jugador(usuario, computadora):
      print(f"La computadora escogio la opcion {computadora}, es {opcion}")
      return '¡Ganaste!'

    if ganó_el_jugador(usuario, computadora) == False:
      print(f"La computadora escogio la opcion {computadora}")
      return '¡Perdiste!'
    

def ganó_el_jugador(jugador, oponente):
    # Retornar True (verdadero) si gana el jugador.
    # Piedra gana a Tijera (pi > ti).
    # Tijera gana a Papel (ti > pa).
    # Papel gana a Piedra (pa > pi).
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())