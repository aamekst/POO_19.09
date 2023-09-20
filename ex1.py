class Carro:
    def __init__ (self,marca,modelo,placa,ano):
        self.marca=marca
        self.modelo=modelo
        self.placa=placa
        self.ano=ano
    
    def exibir(self):
        print(self.marca)
        print(self.modelo)
        print(self.placa)
        print(self.ano)


class Pessoa:
    def __init__(self,nome,idade,carro):
        self.nome=nome
        self.idade=idade
        self.carro=carro



carro1=Carro('honda','honda corse', 'brqert19', '2010')
pessoa1= Pessoa('vitor', 34, carro1)

print(pessoa1.carro.marca)
print(pessoa1.carro.modelo)
print(pessoa1.carro.placa)
print(pessoa1.carro.ano)

pessoa1.carro.exibir()

