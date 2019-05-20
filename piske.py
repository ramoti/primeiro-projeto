class Cliente():
    def __init__(self, nome, email, senha, telefone):
        self.nome= nome
        self.email= email
        self.senha= senha
        self.telefone= telefone

class Produto():
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco= preco

class Animal():
    def __init__(self, nome, especie, dat_nascimento, dono):
        self.nome= nome
        self.especie= especie
        self.dat_nascimento= dat_nascimento
        self,dono= dono
        



if __name__ == "__main__":
    produto= Produto("shampoo de gado(ramos)","R$: 69,90")
    print(produto.nome)
    print(produto.preco)


