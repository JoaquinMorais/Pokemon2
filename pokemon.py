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
        return ( f'{self.name}\nTipo: {self.tipo}\nVida: {self.vida}/{self.vidaTotal} PS\nAtaque: {self.ataque}\nDefensa: {self.defensa}\nVelocidad: {self.velocidad}')
    
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


def Charmander():
    Charmander = Pokemon('Charmander','Fuego',['Arañazo','Ascuas','Mordida','Placaje'],{'Ataque':rd.randint(7,15), 'Defensa':rd.randint(7,13), 'Velocidad':rd.randint(7,15)},rd.randint(39,55),1)
    return Charmander
Squirtle = Pokemon('Squirtle', 'Agua', ['Placaje', 'Latigo', 'Pistola Agua', 'Burbujas'], {'Ataque':rd.randint(6,13), 'Defensa':rd.randint(6,13), 'Velocidad':rd.randint(5,10)},rd.randint(30,47), 1)

        