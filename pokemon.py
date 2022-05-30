
from math import trunc
import random as rd
from re import S
import sys
import time

from movimientos import *

class Pokemon():
    def __init__(self, name, tipo,tipo2, moves, EVs, vida, nivel,evolucion = None):
        
        #, experiencia, ev, nivel_ev, sig_pok, estado
        variacion = 5
        # Guarda variables como atributos
        self.name = name
        self.tipo = tipo
        self.tipo2 = tipo2
        self.moves = moves
        self.ataque = rd.randint(EVs['Ataque']-variacion, EVs['Ataque']+variacion)
        self.defensa = rd.randint( EVs['Defensa']-variacion, EVs['Defensa']+variacion)
        self.ataqueEspecial = rd.randint( EVs['AtaqueEspecial']-variacion, EVs['AtaqueEspecial']+variacion)
        self.defensaEspecial = rd.randint( EVs['DefensaEspecial']-variacion, EVs['DefensaEspecial']+variacion)
        self.velocidad = rd.randint(EVs['Velocidad']-variacion,EVs['Velocidad']+variacion)
        self.vida = rd.randint(vida-variacion,vida+variacion)
        self.vidaTotal = self.vida
        self.nivel = nivel
        self.evolucion = evolucion
        self.status = 'Normal'
        """
        self.experiencia = experiencia
        self.ev = ev
        self.nivel_ev = nivel_ev
        self.sig_pok = sig_pok
        self.estado = estado
        self.vida_1 = 0
        self.vida_2 = 0
        """
    def getStatus(self):
        return ( f'{self.name}\nTipo: {self.tipo}\nVida: {self.vida}/{self.vidaTotal} PS\nNivel: {self.nivel}\nAtaque: {self.ataque}\nDefensa: {self.defensa}\nVelocidad: {self.velocidad}')
    
    def Pegar(self,pos,defensa,defensaEspecial,efectividad):
        movimiento =self.moves[pos]

        if movimiento.tipo in ['Acero','Bicho','Fantasma','Lucha','Normal','Roca','Tierra','Veneno','Volador']:
            Ataque = self.ataque
            Defensa = defensa
        else:
            Ataque = self.ataqueEspecial
            Defensa = defensaEspecial

        bonificacion = 1
        if movimiento.tipo == self.tipo:
            bonificacion = 1.5
        daño = (0.2 * self.nivel)+1
        daño = daño * Ataque * movimiento.potencia
        daño = daño / (25*Defensa)
        daño = (daño+2) * 0.01 * bonificacion * efectividad * rd.randint(85,100) 
        daño = round(daño)
        if daño < 1:
            daño = 1
        return rd.randint(daño,daño+4)
    
    def derrotado(self):
        if self.vida <= 0:
            return True
        else:
            return False
    
    def normalizarVida(self):
        if self.vida <= 0:
            self.vida = 0

    def ventajaTipo(self,pos,tipoEnemigo):
        ataque = self.moves[pos]
        
        # COMPLETOS: Planta Veneno Acero Bicho Electrico Hielo Lucha Roca Volador Dragon Normal


        #Siniestro
        

        if ataque.tipo == 'Acero':
            if tipoEnemigo in ['Fuego','Agua','Electrico','Acero']:
                return 0.5
            if tipoEnemigo in ['Hada','Hielo','Roca']:
                return 2
            
        if ataque.tipo == 'Bicho':
            if tipoEnemigo in ['Acero','Fantasma','Fuego','Hada','Lucha','Veneno','Volador']:
                return 0.5
            if tipoEnemigo in ['Planta','Psiquico','Siniestro']:
                return 2

        if ataque.tipo == 'Electrico':
            if tipoEnemigo in ['Dragon','Electrico','Planta']:
                return 0.5
            if tipoEnemigo in ['Agua','Volador']:
                return 2
            if tipoEnemigo in ['Tierra']:
                return 0
        
        if ataque.tipo == 'Dragon':
            if tipoEnemigo in ['Acero']:
                return 0.5
            if tipoEnemigo in ['Dragon']:
                return 2
            if tipoEnemigo in ['Hada']:
                return 0

        if ataque.tipo == 'Hielo':
            if tipoEnemigo in ['Acero','Agua','Fuego','Hielo']:
                return 0.5
            if tipoEnemigo in ['Dragon','Planta','Tierra','Volador']:
                return 2
        
        if ataque.tipo == 'Lucha':
            if tipoEnemigo in ['Acero','Hielo','Normal','Roca','Siniestro']:
                return 0.5
            if tipoEnemigo in ['Bicho','Hada','Psiquico','Veneno','Volador']:
                return 2
            if tipoEnemigo in ['Fantasma']:
                return 0

        if ataque.tipo == 'Roca':
            if tipoEnemigo in ['Acero','Lucha','Tierra']:
                return 0.5
            if tipoEnemigo in ['Bicho','Fuego','Hielo','Volador']:
                return 2

        if ataque.tipo == 'Tierra':
            if tipoEnemigo in ['Acero','Hielo','Normal','Roca','Siniestro']:
                return 0.5
            if tipoEnemigo in ['Bicho','Hada','Psiquico','Veneno','Volador']:
                return 2
            if tipoEnemigo in ['Fantasma']:
                return 0 

        if ataque.tipo == 'Fuego':
            if tipoEnemigo in ['Agua','Dragon','Fuego','Roca']:
                return 0.5
            if tipoEnemigo in ['Bicho','Acero','Hielo','Planta']:
                return 2

        if ataque.tipo == 'Veneno':
            if tipoEnemigo in ['Bicho','Planta']:
                return 0.5
            if tipoEnemigo in ['Acero','Electrico','Fuego','Roca','Veneno']:
                return 2
            if tipoEnemigo in ['Volador']:
                return 0
        if ataque.tipo == 'Normal':
            if tipoEnemigo in ['Acero','Roca']:
                return 0.5
            if tipoEnemigo in ['Fantasma']:
                return 0

        if ataque.tipo == 'Volador':
            if tipoEnemigo in ['Acero','Electrico','Roca']:
                return 0.5
            if tipoEnemigo in ['Bicho','Lucha','Planta']:
                return 2

        if ataque.tipo == 'Planta':
            if tipoEnemigo in ['Roca']:
                return 2
            if tipoEnemigo in ['Acero','Bicho','Dragon','Veneno','Volador']:
                return 0.5

        version = ['Fuego', 'Agua', 'Planta']
        if ataque.tipo in version and tipoEnemigo in version:
            for i, k in enumerate(version):
                if self.tipo == k:
                    #Ambos son del mismo tipo
                    if tipoEnemigo == k:
                        return 0.5
                            
                    #Pokemon2 es Fuerte
                    if tipoEnemigo == version[(i+1)%3]:
                        return 0.5
                                
                    #Pokemon2 es debil
                    if tipoEnemigo == version[(i+2)%3]:
                        return 2
        return 1
    
    def Evolucionar(self):
        if self.evolucion:
            self.name = self.evolucion.name
            self.moves = self.evolucion.moves
            self.AumentarNivel(nivel=0)
            self.AumentarNivel(nivel=0)
            if self.ataque < self.evolucion.ataque:
                self.ataque = self.evolucion.ataque
            if self.defensa < self.evolucion.defensa:
                self.defensa = self.evolucion.defensa
            if self.ataqueEspecial < self.evolucion.ataqueEspecial:
                self.ataqueEspecial = self.evolucion.ataqueEspecial
            if self.defensaEspecial < self.evolucion.defensaEspecial:
                self.defensaEspecial = self.evolucion.defensaEspecial
            if self.velocidad < self.evolucion.velocidad:
                self.velocidad = self.evolucion.velocidad
            if self.vidaTotal < self.evolucion.vidaTotal:
                vidaAumentar = self.evolucion.vidaTotal - self.vidaTotal
                self.vida += vidaAumentar
                self.vidaTotal += vidaAumentar
            if self.evolucion.tipo2:
                self.tipo2 = self.evolucion.tipo2
            self.evolucion = self.evolucion.evolucion
            return f'Tu Pokemon a evolucionado a {self.name}!!!'
        return 'Tu Pokemon no Puede Evolucionar'


    def AumentarNivel(self,nivel = 1):
        self.nivel += nivel
        self.ataque += rd.randint(0,1)
        self.defensa += rd.randint(0,1)
        self.velocidad += rd.randint(0,2)
        vidaAumentar = rd.randint(1,3)
        self.vida += vidaAumentar
        self.vidaTotal += vidaAumentar
        
    def Revivir(self):
        self.vida = self.vidaTotal
        self.status = 'Normal'

    def MostrarEnPokedex(self):
        txt = ''
        if self.tipo2:
            txt = f' / {self.tipo2}'
        return f'{self.name}\nTipo: {self.tipo + txt}\nVida: {self.vida}/{self.vidaTotal}\nNivel: {self.nivel}\nAtaque: {self.ataque} - Defensa: {self.defensa}\nAtaque Esp: {self.ataqueEspecial} - Defensa Esp: {self.defensaEspecial}\nVelocidad: {self.velocidad}'.center(50)

    def MovimientoEspecial(self,pos):
        if self.moves[pos].caracteristica != 'Normal':
            return True
        return False
    def Cambios(self):
        if self.status == 'Envenenado':
            daño = rd.randint(2,5)
            self.vida -= daño
            printLento(f'{self.name} recibio {daño} de daño por Envenenamiento')
        self.normalizarVida()

    def addVida(self,aumentoVida):
        self.vida += aumentoVida
        if self.vida > self.vidaTotal:
            self.vida = self.vidaTotal
    
    def efectoAlterado(self,posicionAtaque,daño,status):
        statusOtroPokemon = status
        if self.moves[posicionAtaque].precicionEfecto >= rd.randint(1,100):
            if self.moves[posicionAtaque].nombre == 'Polvo Veneno':
                statusOtroPokemon = 'Envenenado'
            if self.moves[posicionAtaque].nombre == 'Drenadoras':
                self.addVida(round(daño/2))
                printLento(f'{self.name} absorbio {round(daño/2)}!!!')
                printLento(f"{self.name} Vida: {self.vida}/{self.vidaTotal}")
                
        else: 
            printLento("No efectuó ningún efecto")

        if statusOtroPokemon != 'Normal':
            printLento(f"{statusOtroPokemon} está {statusOtroPokemon}")
        
        return statusOtroPokemon


def Charizard():
    return Pokemon('Charizard','Fuego','Volador',[Lanzallamas,Infierno,AtaqueAla,Cuchillada], {'Ataque':84, 'Defensa':78,'AtaqueEspecial':109,'DefensaEspecial':85, 'Velocidad':100}, 78, 36)

def Charmeleon():
    return Pokemon('Charmeleon', 'Fuego',None, [Pirotecnea,ColmilloIgneo,GarraMetal,FuriaDragon], {'Ataque':64, 'Defensa':58,'AtaqueEspecial':80,'DefensaEspecial':65, 'Velocidad':80}, 58, 16,evolucion=Charizard())

def Charmander():
    return Pokemon('Charmander','Fuego',None,[Arañazo,Ascuas,GarraMetal,FuriaDragon],{'Ataque':52, 'Defensa':43,'AtaqueEspecial':60,'DefensaEspecial':50, 'Velocidad':65},39,1,evolucion=Charmeleon())

    

def Wartortle():
    return Pokemon('Wartortle','Agua',None,[Mordisco,Cabezazo,AcuaCola,Hidropulso],{'Ataque':63, 'Defensa':80,'AtaqueEspecial':65,'DefensaEspecial':80, 'Velocidad':58},59,16,)

def Squirtle():
    return Pokemon('Squirtle', 'Agua',None, [Placaje,PistolaAgua,Burbuja,Mordisco], {'Ataque':48, 'Defensa':65,'AtaqueEspecial':50,'DefensaEspecial':64, 'Velocidad':43},44, 1, evolucion=Wartortle())



def Ivysaur():
    return Pokemon('Ivysaur','Planta','Veneno',[DobleFilo,PolvoVeneno,HojaAfilada,LatigoCepa],{'Ataque':62, 'Defensa':63,'AtaqueEspecial':80,'DefensaEspecial':80, 'Velocidad':60},60,16)
def Bulbasaur():
    return Pokemon('Bulbasaur', 'Planta','Veneno', [Placaje, LatigoCepa, Drenadoras, Derribo], {'Ataque':49, 'Defensa':49,'AtaqueEspecial':65,'DefensaEspecial':65, 'Velocidad':45},45, 1,evolucion=Ivysaur())



def MegaLucario():
    return Pokemon('Mega Lucario', 'Lucha','Acero', [ABocarrajo, VelocidadExtrema, PuñoIncremento, PulsoDragon], {'Ataque':145, 'Defensa':88,'AtaqueEspecial':140,'DefensaEspecial':70, 'Velocidad':112},70, 55)
def Lucario():
    return Pokemon('Lucario', 'Lucha','Acero', [PuñoIncremento,PulsoDragon,EsferaAura, GarraMetal], {'Ataque':110, 'Defensa':70,'AtaqueEspecial':115,'DefensaEspecial':70, 'Velocidad':90},70, 30,evolucion=MegaLucario())
def Riolu():
    return Pokemon('Riolu', 'Lucha',None, [EsferaAura, GarraMetal, AtaqueRapido, Amago], {'Ataque':70, 'Defensa':40,'AtaqueEspecial':35,'DefensaEspecial':40, 'Velocidad':60},40, 1,evolucion=Lucario())

































def IniciarJuego():
    print('             _                              ')
    print('            | |                             ')
    print(' _ __   ___ | | _____ _ __ ___   ___  _ __  ')
    print("|  _ \ / _ \| |/ / _ \  _ ` _ \ / _ \|  _ \ ")
    print('| |_) | (_) |   <  __/ | | | | | (_) | | | |')
    print('| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|')
    print('| |                                         ')
    print('|_|                                         ')



def printLento(s, delay=0.04):
    if s:
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        print()



def getPokemon(n):
    if n == "1":
        return Bulbasaur()
    elif n == "2":
        return Ivysaur()
    elif n == "3":
        return Ivysaur()

    elif n == "4":
        return Charmander()
    elif n == "5":
        return Charmeleon()
    elif n == "6":
        return Charizard()

    elif n == "7":
        return Squirtle()
    elif n == "8":
        return Wartortle()
    elif n == "9":
        return Wartortle()

    elif n == "10":
        return Riolu()
    elif n == "11":
        return Lucario()
    elif n == "12":
        return MegaLucario()
    else:
        return Riolu()