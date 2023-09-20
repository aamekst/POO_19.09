class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(p.descricao, p.valor)

    def calcular_total(self):
        soma = 0
        for p in self.produtos:
            soma += p.valor
        print(f'Total: {soma}')

cliente1 = Cliente('joao')
cliente2 = Cliente('ana')

prod1 = Produto('caneta', 5.0)
prod2 = Produto('caderno', 30.0)
prod3 = Produto('pincel', 5.0)

print(cliente1.nome)
carrinho = Carrinho(cliente1)
carrinho.adicionar_produtos(prod1)
carrinho.adicionar_produtos(prod2)
carrinho.adicionar_produtos(prod3)

carrinho.listar_produtos()

carrinho.calcular_total()
print('------------------')

print(cliente2.nome)
carrinho = Carrinho(cliente2)
carrinho.adicionar_produtos(prod2)
carrinho.adicionar_produtos(prod2)
carrinho.adicionar_produtos(prod2)

carrinho.listar_produtos()

carrinho.calcular_total()
