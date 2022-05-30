class Movimientos():
    def __init__(self,nombre,tipo,potencia,precision,caracteristica = 'Normal',precicionEfecto = 100):
        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.precision = precision
        self.caracteristica = caracteristica
        self.precicionEfecto = precicionEfecto
    def __str__(self):
        return self.nombre


Arañazo = Movimientos('Arañazo','Normal',40,100)
Ascuas = Movimientos('Ascuas','Fuego',40,100)
FuriaDragon = Movimientos('Furia Dragon','Dragon',55,90)
GarraMetal = Movimientos('Garra Metal','Acero',50,90)
ColmilloIgneo = Movimientos('Colmillo Igneo','Fuego',65,95)
Pirotecnea = Movimientos('Pirotecnea','Fuego',70,90)
Lanzallamas = Movimientos('Lanzallamas','Fuego',90,100,'Fuego',10)
Infierno = Movimientos('Infierno','Fuego',100,50,'Fuego',100)
AtaqueAla = Movimientos('Ataque Ala','Volador',60,100)
Cuchillada = Movimientos('Cuchillada','Normal',60,100)

Placaje = Movimientos('Placaje','Normal',40,100)
PistolaAgua = Movimientos('Pistola Agua','Agua',50,90)
Burbuja = Movimientos('Burbuja','Agua',40,100)
Mordisco = Movimientos('Mordisco','Siniestro',60,95)
Hidropulso = Movimientos('Hidropulso','Agua',60,100)
AcuaCola = Movimientos('Acua Cola','Agua',90,90)
Cabezazo = Movimientos('Cabezazo','Normal',130,80)

Drenadoras = Movimientos('Drenadoras','Planta',10,100,'Regenerar')
LatigoCepa = Movimientos('Latigo Cepa','Planta',45,100)
Derribo = Movimientos('Derribo','Normal',90,80)
HojaAfilada = Movimientos('Hoja Afilada','Planta',65,100)
DobleFilo = Movimientos('Doble Filo','Normal',130,90)

PolvoVeneno = Movimientos('Polvo Veneno','Veneno',0,100,'Envenenar',75)









