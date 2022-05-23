class Pokemon():
    def __init__(self, name, tipo, moves, EVs, vida, nivel):
        
        #, experiencia, ev, nivel_ev, sig_pok, estado

        # Guarda variables como atributos
        self.name = name
        self.tipo = tipo
        self.moves = moves
        self.ataque = EVs['Ataque']
        self.defensa = EVs['Defensa']
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
        print( f'{self.name}\nTipo: {self.tipo}\n{self.vida}/{self.vidaTotal} PS')
    