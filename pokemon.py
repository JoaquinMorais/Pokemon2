from math import trunc
import random as rd

from movimientos import *

class Pokemon():
    def __init__(self, name, tipo, moves, EVs, vida, nivel):
        
        #, experiencia, ev, nivel_ev, sig_pok, estado

        # Guarda variables como atributos
        self.name = name
        self.tipo = tipo
        self.moves = moves
        self.ataque = EVs['Ataque']
        self.defensa = EVs['Defensa']
        self.velocidad = EVs['Velocidad']
        self.vida = vida
        self.nivel = nivel

        self.vidaTotal = self.vida
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
    
    def Pegar(self,pos,defensa):
        ataque =self.moves[pos]
        daño = trunc(((self.ataque+(ataque.potencia/15))/100) * (100-defensa))
        daño = rd.randint(daño-3,daño+3)
        if daño < 1:
            daño = 1
        return daño
    
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
                    










def Charmander():
    Charmander = Pokemon('Charmander','Fuego',[Arañazo,Ascuas,GarraMetal,FuriaDragon],{'Ataque':52, 'Defensa':43, 'Velocidad':65},39,1)
    return Charmander
def Squirtle():
    Squirtle = Pokemon('Squirtle', 'Agua', [Placaje,PistolaAgua,Burbuja,Mordisco], {'Ataque':48, 'Defensa':65, 'Velocidad':43},44, 1)
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
