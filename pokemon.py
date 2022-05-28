from bdb import effective
from math import trunc
import random as rd

from movimientos import *

class Pokemon():
    def __init__(self, name, tipo, moves, EVs, vida, nivel,evolucion = None):
        
        #, experiencia, ev, nivel_ev, sig_pok, estado
        variacion = 5
        # Guarda variables como atributos
        self.name = name
        self.tipo = tipo
        self.moves = moves
        self.ataque = rd.randint(EVs['Ataque']-variacion, EVs['Ataque']+variacion)
        self.defensa = rd.randint( EVs['Defensa']-variacion, EVs['Defensa']+variacion)
        self.velocidad = rd.randint(EVs['Velocidad']-variacion,EVs['Velocidad']+variacion)
        self.vida = rd.randint(vida-variacion,vida+variacion)
        self.vidaTotal = self.vida
        self.nivel = nivel
        self.evolucion = evolucion
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
    
    def Pegar(self,pos,defensa,efectividad):
        ataque =self.moves[pos]
        bonificacion = 1
        if ataque.tipo == self.tipo:
            bonificacion = 1.5
        daño = (0.2 * self.nivel)+1
        daño = daño * self.ataque * ataque.potencia
        daño = daño / (25*defensa)
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
        
        if ataque.tipo == 'Normal' or ataque.tipo == 'Siniestro' or ataque.tipo == 'Dragon':
            return 1,''
        if ataque.tipo == 'Acero':
            if tipoEnemigo == 'Fuego' or tipoEnemigo == 'Agua':
                return 0.5,'No es muy efectivo...'
            else:
                return 1,''
            
        version = ['Fuego', 'Agua', 'Planta']
        if ataque.tipo in version and tipoEnemigo in version:
            for i, k in enumerate(version):
                if self.tipo == k:
                    #Ambos son del mismo tipo
                    if tipoEnemigo == k:
                        return 1,''
                            
                    #Pokemon2 es Fuerte
                    if tipoEnemigo == version[(i+1)%3]:
                        return 0.5,'No es muy efectivo...'
                                
                    #Pokemon2 es debil
                    if tipoEnemigo == version[(i+2)%3]:
                        return 2,'Es super efectivo!'
    
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
            if self.velocidad < self.evolucion.velocidad:
                self.velocidad = self.evolucion.velocidad
            if self.vida < self.evolucion.vida:
                vidaAumentar = self.evolucion.vida - self.vida
                self.vida += vidaAumentar
                self.vidaTotal += vidaAumentar
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






def Charmeleon():
    Charmeleon = Pokemon('Charmeleon', 'Fuego', [Pirotecnea,ColmilloIgneo,GarraMetal,FuriaDragon], {'Ataque':64, 'Defensa':58, 'Velocidad':80}, 58, 16)
    return Charmeleon
def Charmander():
    Charmander = Pokemon('Charmander','Fuego',[Arañazo,Ascuas,GarraMetal,FuriaDragon],{'Ataque':52, 'Defensa':43, 'Velocidad':65},39,1,evolucion=Charmeleon())
    return Charmander
    
def Wartortle():
    Wartortle = Pokemon('Wartortle','Agua',[Mordisco,Cabezazo,AcuaCola,Hidropulso],{'Ataque':63, 'Defensa':80, 'Velocidad':58},59,16,)
    return Wartortle
def Squirtle():
    Squirtle = Pokemon('Squirtle', 'Agua', [Placaje,PistolaAgua,Burbuja,Mordisco], {'Ataque':48, 'Defensa':65, 'Velocidad':43},44, 1, evolucion=Wartortle())
    return Squirtle

def Bulbasaur():
    Bulbasaur = Pokemon('Bulbasaur', 'Planta', [Placaje, LatigoCepa, Drenadoras, Derribo], {'Ataque':49, 'Defensa':49, 'Velocidad':45},45, 1)
    return Bulbasaur





def IniciarJuego():
    print('             _                              ')
    print('            | |                             ')
    print(' _ __   ___ | | _____ _ __ ___   ___  _ __  ')
    print(f"|  _ \ / _ \| |/ / _ \  _ ` _ \ / _ \|  _ \ ")
    print('| |_) | (_) |   <  __/ | | | | | (_) | | | |')
    print(f'| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|')
    print('| |                                         ')
    print('|_|                                         ')
