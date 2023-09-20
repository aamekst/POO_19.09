#associação de classes
class Endereco:
    def __init__ (self, rua, numero, cep):
        self.rua=rua
        self.numero = numero
        self.cep=cep
    
    def exibir(self):#metodo para mostras todos os atributos
        print(self.numero)
        print(self.rua)
        print(self.cep)

class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome=nome
        self.idade=idade
        self.endereco= endereco

end1 = Endereco('Rua Silvinha', 123, '12345-000')
pessoa1 = Pessoa('Alaninhaa', 19, end1)#associação entre as classes (end1-objeto e pessoa1)

print(pessoa1.endereco.rua)
pessoa1.endereco.rua = 'casa do caraio' # modificando o endereço
print(pessoa1.endereco.rua)
print(pessoa1.endereco.cep)
print(pessoa1.endereco.numero)

pessoa2 = Pessoa('ana', 40, end1)

pessoa1.endereco.exibir()#chama o metodo 
