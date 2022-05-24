import random as rd

from pyparsing import Char
from pokemon import *
import time
import numpy as np
import sys
from math import trunc




def Combate():
    printLento(f"Preparate a un desafio a manos de... ¡Entrenador Rojo!")
    printLento(f"Entrenador Rojo saca a {Pokemon2.name}")
    printLento(f"Adelante, {Pokemon1.name}")
    mostrarCaracteristicas()
    if Pokemon1.velocidad < Pokemon2.velocidad:
        Pelear("ataqueEnemigo")
    while True:
        
        if Pokemon1.derrotado():
            printLento(f"{Pokemon1.name} ha sido derrotado")
            break
        
        Pelear("ataqueMio")
        if Pokemon2.derrotado():
            printLento(f"{Pokemon2.name} ha sido derrotado")
            break
        time.sleep(0.5)
        printLento("...")
        time.sleep(0.5)
        
        Pelear("ataqueEnemigo")
        

def Pelear(modo):
    if modo == "ataqueMio":
        printLento(f"Elige un ataque\n1) {Pokemon1.moves[0]}, 2) {Pokemon1.moves[1]}\n3) {Pokemon1.moves[2]}, 4) {Pokemon1.moves[3]}")
        num = str(input(">> "))
        if num in ["1","2","3","4"]:
           ataque = Pokemon1.moves[int(num)-1] 
        else:
            ataque = Pokemon1.moves[0] 
        printLento(f"¡{Pokemon1.name} usa {ataque}!")
        daño = Pokemon1.Pegar(Pokemon2.defensa)
        printLento(f"{Pokemon2.name} recibe {daño} de daño")
        Pokemon2.vida -= daño
        Pokemon2.normalizarVida()
        printLento(f"{Pokemon2.name} Vida: {Pokemon2.vida}/{Pokemon2.vidaTotal}")

    if modo == "ataqueEnemigo":
        ataque = Pokemon2.moves[rd.randint(0,3)]
        printLento(f"{Pokemon2.name} uso {ataque}!!!")
        daño = Pokemon2.Pegar(Pokemon1.defensa)
        printLento(f"{Pokemon1.name} recibe {daño} de daño")
        Pokemon1.vida -= daño
        Pokemon1.normalizarVida()
        printLento(f"{Pokemon1.name} Vida: {Pokemon1.vida}/{Pokemon1.vidaTotal}")




def printLento(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def mostrarCaracteristicas():
    printLento("----- Batalla Pokemon -----")
    printLento(f"{Pokemon1.getStatus()}")
    printLento("VS")
    printLento(f"{Pokemon2.getStatus()}")




Pokemon1 = Charmander()
Pokemon2 = Charmander()

Combate()
