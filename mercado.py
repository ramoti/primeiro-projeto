import peewee, os

db = peewee.SqliteDatabase ("animalia.db")

class Animal(peewee.Model):

    nomedono = peewee.CharField()
    tipo animal = peewee.CharField ()
    raca = peewee.CharField ()
    class Meta:

        database = db

    def str ( self ) :
        return self.tipo animal+","+ self.raca+" de "+ self.nomedono

class Consulta(peewee.Model):
    data = peewee.CharField ()
    servico = peewee.CharField ()
    horario = peewee.CharField ()
    confirma = peewee.CharField ()
    myID = peewee.CharField()

    class Meta:

    database = db

    def str ( self ) :
        return self.servico +" em "+ self.data+": "+ self.horario+", confirmado: "+ "\n" self.confirma+", ID da consulta : "+ self.myID+" | animal: "+str(self.animal)







if __name__ == "__main__":
    