import random as rd
from pokemon import Pokemon




Charmander = Pokemon('Charmander','Fuego',['Arañazo','Ascuas','Mordida','Placaje'],{'Ataque':rd.randint(7,10), 'Defensa':rd.randint(7,13)},rd.randint(39,55),1)
Squirtle = Pokemon('Squirtle', 'Agua', ['Placaje', 'Latigo', 'Pistola Agua', 'Burbujas'], {'Ataque':rd.randint(6,13), 'Defensa':rd.randint(6,13)},rd.randint(30,47), 1)



Pokemon1 = Charmander
Pokemon2 = Squirtle


def Pelear():
    Pokemon1.getStatus()
    print('Vs')
    Pokemon2.getStatus()




