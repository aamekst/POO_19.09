class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        soma = 0
        for p in self.produtos:
            soma += p.preco * p.quantidade
        print(f'Total: {soma}')

class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade



cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)


print(cafe.nome)
print(cafe.preco)
print(cafe.quantidade)
print('---------------')
print(arroz.nome)
print(arroz.preco)
print(arroz.quantidade)
print('---------------')
print(feijao.nome)
print(feijao.preco)
print(feijao.quantidade)
print('---------------')
meu_pedido.calcular_valor()

