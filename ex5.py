def main():
    moto = Moto("Yahama XPTO-100", MecanismoDeAceleracaoDeMotos())
    carro = Carro("Honda Fit", MecanismoDeAceleracaoDeCarros())
    listaAutomoveis = [moto, carro]
    for automovel in listaAutomoveis:
        automovel.acelerar()
        automovel.acenderFarol()