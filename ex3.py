# As classes dentro do parênteses são as classes mãe da classe sendo definida
class HondaFit(Carro):

    def __init__(self, mecanismoAceleracao):
        modelo = "Honda Fit"
        # chama o construtor da classe mãe, ou seja, da classe "Carro"
        super().__init__(self, modelo, mecanismoAceleracao)