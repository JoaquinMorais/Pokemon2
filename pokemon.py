from math import trunc
import random as rd
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
    
    def Pegar(self,defensa):
        daño = trunc((self.ataque/100) * (100-defensa))+1
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

    def ventajaTipo(self,tipoEnemigo):
        version = ['Fuego', 'Agua', 'Planta']
        for i, k in enumerate(version):
            if self.tipo == k:
            #Ambos son del mismo tipo
                if tipoEnemigo == k:
                    return 1,''
                        
            #Pokemon2 es Fuerte
                if tipoEnemigo == version[(i+1)%3]:
                    print(version[(i+1)%3])
                    
                    return 0.5,'No es muy efectivo...'
                    
                    
                        
                #Pokemon2 es debil
                if tipoEnemigo == version[(i+2)%3]:
                    
                    return 2,'Es super efectivo!'
                    


def IniciarJuego():
    print('             _                              ')
    print('            | |                             ')
    print(' _ __   ___ | | _____ _ __ ___   ___  _ __  ')
    print(f"|  _ \ / _ \| |/ / _ \  _ ` _ \ / _ \|  _ \ ")
    print('| |_) | (_) |   <  __/ | | | | | (_) | | | |')
    print(f'| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|')
    print('| |                                         ')
    print('|_|                                         ')


def Charmander():
    Charmander = Pokemon('Charmander','Fuego',['Arañazo','Ascuas','Mordida','Placaje'],{'Ataque':rd.randint(7,15), 'Defensa':rd.randint(7,12), 'Velocidad':rd.randint(7,15)},rd.randint(33,45),1)
    return Charmander
def Squirtle():
    Squirtle = Pokemon('Squirtle', 'Agua', ['Placaje', 'Latigo', 'Pistola Agua', 'Burbujas'], {'Ataque':rd.randint(6,13), 'Defensa':rd.randint(7,13), 'Velocidad':rd.randint(5,10)},rd.randint(27,42), 1)
    return Squirtle
def Bulbasaur():
    Bulbasaur = Pokemon('Bulbasaur', 'Planta', ['Placaje', 'Latigo Cepa', 'Bomba Lodo', 'Latigazo'], {'Ataque':rd.randint(5,10), 'Defensa':rd.randint(9,15), 'Velocidad':rd.randint(4,8)},rd.randint(36,49), 1)
    return Bulbasaur





