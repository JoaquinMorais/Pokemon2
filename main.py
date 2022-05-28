import random as rd
from re import S

from pyparsing import Char
import time
import sys
from math import trunc

from pokemon import *
from drawPokemon import *
from movimientos import *



########## PELEAS ##########
def IniciarCombate():
    printLento(f"Preparate a un desafio a manos de... ¡Entrenador Rojo!")
    printLento(f"Entrenador Rojo saca a {Pokemon2.name}")
    printLento(f"Adelante, {Pokemon1.name}")
    #mostrarCaracteristicas()
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
        printLento("...",0.1)
        time.sleep(0.5)
        
        Pelear("ataqueEnemigo")
        

def Pelear(modo):
    if modo == "ataqueMio":
        printLento(f"Elige un ataque\n1) {Pokemon1.moves[0]}, 2) {Pokemon1.moves[1]}\n3) {Pokemon1.moves[2]}, 4) {Pokemon1.moves[3]}")
        num = str(input(">> "))
        if num in ["1","2","3","4"]:
           ataque = int(num)-1
        else:
            ataque = 0
        printLento(f"¡{Pokemon1.name} usa {Pokemon1.moves[ataque]}!")
        EfectividadAtaque,txt = Pokemon1.ventajaTipo(ataque,Pokemon2.tipo)
        daño = Pokemon1.Pegar(ataque,Pokemon2.defensa,EfectividadAtaque)
        printLento(txt)
        printLento(f"{Pokemon2.name} recibe {daño} de daño")
        Pokemon2.vida -= daño
        Pokemon2.normalizarVida()
        printLento(f"{Pokemon2.name} Vida: {Pokemon2.vida}/{Pokemon2.vidaTotal}")

    if modo == "ataqueEnemigo":
        ataque = rd.randint(0,3)
        printLento(f"{Pokemon2.name} uso {Pokemon2.moves[ataque]}!!!")
        EfectividadAtaque,txt = Pokemon2.ventajaTipo(ataque,Pokemon1.tipo)
        daño = Pokemon2.Pegar(ataque,Pokemon1.defensa,EfectividadAtaque)
        printLento(txt)
        printLento(f"{Pokemon1.name} recibe {daño} de daño")
        Pokemon1.vida -= daño
        Pokemon1.normalizarVida()
        printLento(f"{Pokemon1.name} Vida: {Pokemon1.vida}/{Pokemon1.vidaTotal}")

def mostrarCaracteristicas():
    printLento("----- Batalla Pokemon -----")
    printLento(f"{Pokemon1.getStatus()}")
    printLento("VS")
    printLento(f"{Pokemon2.getStatus()}")



### PRINTS ###
def printLento(s, delay=0.04):
    if s:
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        print()
def printListaLento(l, delay=0.04):
    for s in l:
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        print()

########## Menu ##########
def Menu():
    printLento("----- Menu -----")
    printLento("1) Jugar")
    printLento("2) Evolucionar")
    printLento("3) Salir")
    num = str(input(">> "))
    if num == "1":
        Pokemon1.Revivir()
        Pokemon2.Revivir()
        IniciarCombate()
    if num == "2":
        txt = Pokemon1.Evolucionar()
        printLento(txt)
    elif num == "3":
        printLento("Cerrando Juego...",0.08)
        time.sleep(1)
        sys.exit()
    else:
        Menu()

########## MAIN ##########
def Main(intro = True):
    if intro:
        printLento("Iniciando Juego... Espere unos segundos")
        time.sleep(2)
        IniciarJuego()
        time.sleep(2)
    while True:
        Menu()


Pokemon1 = Squirtle()
Pokemon2 = Charmander()



Main(False)




