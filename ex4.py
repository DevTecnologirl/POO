class Automovel():
    def acelerar(self):
        raise NotImplementedError()

    def frear(self):
        raise NotImplementedError()

    def acenderFarol(self):
        raise NotImplementedError()

class Carro(Automovel):

    # ...

    def acelerar(self):
        # Codigo para acelerar o carro

    def frear(self):
        # Codigo para frear o carro

    def acenderFarol(self):
        # Codigo para acender o farol do carro

    # ...

class Moto(Automovel):

    # ...

    def acelerar(self):
        # Codigo para acelerar a moto

    def frear(self):
        # Codigo para frear a moto

    def acenderFarol(self):
        # Codigo para acender a moto

    # ...