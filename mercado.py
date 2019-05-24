class Produto():
    def __init__(self,nome_produto, valor_produto):
        self.nome_produto= nome_produto
        self.valor_produto= valor_produto


    
class Item():
    def __init__(self, produto, quantidade):
        self.produto= produto
        self.quantidade= quantidade



class Carrinho():

    def __init__(self, lista_itens):
        self.lista_itens= lista_itens
    
    def mostra_carrinho(self):
        print("_______LISTA________")
        print()
        val_total=0
        num=0
        for produto in self.lista_itens:
            print(self.lista_itens[num].produto.nome_produto)
            valor= self.lista_itens[num].produto.valor_produto * self.lista_itens[num].quantidade
            val_total+= valor
            num+=1
            print("valor total do seu produto: ", valor)
            print()
        print()
        print("valor total: ", val_total)

if __name__ == "__main__":
    produto1= Produto("carne", 0.75)
    produto2= Produto("batata doce", 3.50)
    item= Item(produto1, 2)
    item2= Item(produto2, 1.750)
    carrinho= Carrinho([item,item2])
    carrinho.mostra_carrinho()