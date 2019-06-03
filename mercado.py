import peewee, os

db = peewee.SqliteDatabase ( ’ animalia.db’)

class Animal(peewee.Model):

    nomedono = peewee.CharField()
    tipo animal = peewee.CharField ()
    raca = peewee.CharField ()
    class Meta:

        database = db

    def str ( self ) :
        return self . tipo animal+”,”+ self . raca+” de ”+ self .nomedono

class Consulta(peewee.Model):
    data = peewee.CharField ()
    servico = peewee.CharField ()
    horario = peewee.CharField ()
    confirma = peewee.CharField ()
    myID = peewee.CharField()

    class Meta:

    database = db

    def str ( self ) :
        return self . servico +" em "+ self .data+": "+ self . horario+", confirmado: "+ "\n" self . confirma+”, ID da consulta : ”+ self .myID+” | animal: ”+str( self .animal)







if __name__ == "__main__":
    produto1= Produto("carne", 0.75)
    produto2= Produto("batata doce", 3.50)
    item= Item(produto1, 2)
    item2= Item(produto2, 1.750)
    carrinho= Carrinho([item,item2])
    carrinho.mostra_carrinho()