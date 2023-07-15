# Exemplo da classe Carro em Python
class Carro:
    def __init__(self, modelo, mecanismoAceleracao):
        self.__modelo = modelo;
        self.__velocidade = 0
        self.__mecanismoAceleracao = mecanismoAceleracao

    def acelerar(self):
        mecanismoAceleracao.acelerar()

    def frear(self):
        # Codigo para frear o carro

    def acenderFarol(self):
        # Codigo para acender o farol do carro

    def getVelocidade(self):
        return self.velocidade

    def __setVelocidade(self):
        # Codigo para alterar a velocidade por dentro do objeto

    def getModelo(self):
        return self.modelo

    def getCor(self):
        return self.cor

    def setCor(self, cor):
        self.cor = cor