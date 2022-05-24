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
        