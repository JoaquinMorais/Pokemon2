class Movimientos():
    def __init__(self,nombre,tipo,potencia,precision):
        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.precision = precision
    def __str__(self):
        return self.nombre


Arañazo = Movimientos('Arañazo','Normal',40,100)
Ascuas = Movimientos('Ascuas','Fuego',40,100)
FuriaDragon = Movimientos('Furia Dragon','Dragon',55,90)
GarraMetal = Movimientos('Garra Metal','Acero',50,90)
ColmilloIgneo = Movimientos('Colmillo Igneo','Fuego',65,95)
Pirotecnea = Movimientos('Pirotecnea','Fuego',70,90)

Placaje = Movimientos('Placaje','Normal',40,100)
PistolaAgua = Movimientos('Pistola Agua','Agua',50,90)
Burbuja = Movimientos('Burbuja','Agua',40,100)
Mordisco = Movimientos('Mordisco','Siniestro',60,95)
Hidropulso = Movimientos('Hidropulso','Agua',60,100)
AcuaCola = Movimientos('Acua Cola','Agua',90,90)
Cabezazo = Movimientos('Cabezazo','Normal',130,80)

Drenadoras = Movimientos('Drenadoras','Planta',10,100)
LatigoCepa = Movimientos('Latigo Cepa','Planta',45,100)
Derribo = Movimientos('Derribo','Normal',90,80)

