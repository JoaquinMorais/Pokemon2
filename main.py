import random as rd

import time
import sys
import os
from math import trunc

from pokemon import *
from drawPokemon import *
from movimientos import *

### Cosas Extra ###
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
def clear():
    os.system('cls')

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
            printLento(f"{Pokemon1.name} ha sido derrotado...")
            break
        
        Pelear("ataqueMio")
        if Pokemon2.derrotado():
            printLento(f"{Pokemon2.name} ha sido derrotado!!!")
            break
        
        Pelear("ataqueEnemigo")
        

def Pelear(modo):
    daño = 0
    if modo == "ataqueMio":
        diferenciaLetras1 =""
        diferenciaLetras2 =""
        if len(Pokemon1.moves[0].nombre) > len(Pokemon1.moves[2].nombre):
            diferenciaLetras2 = " "*(len(Pokemon1.moves[0].nombre) - len(Pokemon1.moves[2].nombre))
        elif len(Pokemon1.moves[0].nombre) < len(Pokemon1.moves[2].nombre):
            diferenciaLetras1 = " "*(len(Pokemon1.moves[2].nombre) - len(Pokemon1.moves[0].nombre))
        ataque = mostrarAtaques(diferenciaLetras1,diferenciaLetras2)
        printLento(f"¡{Pokemon1.name} usa {Pokemon1.moves[ataque]}!")
        
        
        
        if Pokemon1.moves[ataque].potencia != 0:
            EfectividadAtaque,txt = Pokemon1.ventajaTipo(ataque,Pokemon2.tipo)
            daño = Pokemon1.Pegar(ataque,Pokemon2.defensa,Pokemon2.defensaEspecial,EfectividadAtaque)
            printLento(txt)
            printLento(f"{Pokemon2.name} recibe {daño} de daño")
            Pokemon2.vida -= daño

        if Pokemon1.MovimientoEspecial(ataque):
            efectoAlterado(1,ataque,daño)

        Pokemon2.Cambios()
        printLento(f"{Pokemon2.name} Vida: {Pokemon2.vida}/{Pokemon2.vidaTotal}")

    if modo == "ataqueEnemigo":
        time.sleep(0.5)
        printLento("...",0.1)
        time.sleep(0.5)
        ataque = rd.randint(0,3)
        printLento(f"{Pokemon2.name} uso {Pokemon2.moves[ataque]}!!!")

        
        if Pokemon2.moves[ataque].potencia != 0:
            EfectividadAtaque,txt = Pokemon2.ventajaTipo(ataque,Pokemon1.tipo)
            daño = Pokemon2.Pegar(ataque,Pokemon1.defensa,Pokemon1.defensaEspecial,EfectividadAtaque)
            printLento(txt)
            printLento(f"{Pokemon1.name} recibe {daño} de daño")
            Pokemon1.vida -= daño

        if Pokemon2.MovimientoEspecial(ataque):
            efectoAlterado(2,ataque,daño)

        Pokemon1.Cambios()
        printLento(f"{Pokemon1.name} Vida: {Pokemon1.vida}/{Pokemon1.vidaTotal}")

def efectoAlterado(modo,posicionAtaque,daño = 0):
    if modo == 1:
        if Pokemon1.moves[posicionAtaque].precicionEfecto >= rd.randint(1,100):
            if Pokemon1.moves[posicionAtaque].nombre == 'Polvo Veneno':
                Pokemon2.status = 'Envenenado'
            if Pokemon1.moves[posicionAtaque].nombre == 'Drenadoras':
                Pokemon1.addVida(daño)
                printLento(f'{Pokemon1.name} absorbio {daño}!!!')
                printLento(f"{Pokemon1.name} Vida: {Pokemon1.vida}/{Pokemon1.vidaTotal}")
                
        else: 
            printLento("No efectuó ningún efecto")

        if Pokemon2.status != 'Normal':
            printLento(f"{Pokemon2.name} está {Pokemon2.status}")
        
    if modo == 2:
        if Pokemon2.moves[posicionAtaque].precicionEfecto >= rd.randint(1,100):
            if Pokemon2.moves[posicionAtaque].nombre == 'Polvo Veneno':
                Pokemon1.status = 'Envenenado'
            if Pokemon2.moves[posicionAtaque].nombre == 'Drenadoras':
                Pokemon2.addVida(daño)
                printLento(f'{Pokemon2.name} absorbio {daño}!!!')
                printLento(f"{Pokemon2.name} Vida: {Pokemon2.vida}/{Pokemon2.vidaTotal}")
        else: 
            printLento("No efectuó ningún efecto")

        if Pokemon1.status != 'Normal':
            printLento(f"{Pokemon1.name} está {Pokemon1.status}")


def mostrarCaracteristicas():
    printLento("----- Batalla Pokemon -----")
    printLento(f"{Pokemon1.getStatus()}")
    printLento("VS")
    printLento(f"{Pokemon2.getStatus()}")

def mostrarAtaques(difer1, difer2):
    while True:
        printLento(f"Elige un ataque\n1) {Pokemon1.moves[0]} {difer1} 2) {Pokemon1.moves[1]}")
        printLento(f"3) {Pokemon1.moves[2]} {difer2} 4) {Pokemon1.moves[3]}")
        num = str(input(">> "))
        if num in ["1","2","3","4"]:
            break
    return int(num)-1
    


########## Menu ##########
def Menu():
    time.sleep(2)
    clear()
    printLento("----- Menu -----")
    printLento("1) Jugar")
    printLento("2) Evolucionar")
    printLento("3) Pokedex")
    printLento("4) Salir")
    num = str(input(">> "))
    if num in ["1","2","3","4"]:
        clear()
    if num == "1":
        Pokemon1.Revivir()
        Pokemon2.Revivir()
        IniciarCombate()
    if num == "2":
        txt = Pokemon1.Evolucionar()
        printLento(txt)
    if num == "3":
        txt = Pokemon1.MostrarEnPokedex()
        printLento(txt)
    elif num == "4":
        printLento("Cerrando Juego...",0.08)
        time.sleep(1)
        clear()
        sys.exit()
    else:
        Menu()

########## MAIN ##########
def Main(intro = True):
    if intro:
        printLento("Iniciando Juego... Espere unos segundos")
        time.sleep(2)
        IniciarJuego()

    while True:
        Menu()


Pokemon1 = Bulbasaur()
Pokemon2 = Charmeleon()



Main()




