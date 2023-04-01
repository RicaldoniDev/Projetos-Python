import random

class Personagem():

    def __init__(self, nome:str, arma:str, armadura:str, escudo:bool, bonus:dict):
        self.nome = nome
        self.arma = arma
        self.armadura = armadura
        self.escudo = escudo
        self.vida = random.randint(1, 20) + self.bonus['ataque']
        self.ataque = random.randint(1, 20) + self.bonus['destreza']
        self.destreza = random.randrange(50, 250, 50) + self.bonus['vida']
        self.bonus = bonus
