import peewee, os

db = peewee.SqliteDatabase()

class Animal(peewee.Model):

    nomedono = peewee.CharField()
    animal = peewee.CharField ()
    raca = peewee.CharField ()

    class Meta:
        database = db

    def __str__(self) :
        return self.tipo_animal+ ","+ self.raca+","+self.nomedono+"."


class Consulta(peewee.Model):

    data = peewee.CharField ()
    servico = peewee.CharField ()
    horario = peewee.CharField ()
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField ()
    myID = peewee.CharField()

    class Meta:

        database = db

    class __st__(self):

        return self.servico +"em"+self.data+":"+ self.horario+",confirmado:"+ "\n" self.confirma + ",ID da consulta: " + self.myID +"| animal: " + str(self.animal)

if __name__ == "__main__":

    arq= "animalia.db"
    if os.path.exists(arq):
        os.remove(arq)
    
    try:

        db.connect()
        db.create.tables([Animal,Consulta])
    
    except peewere.OperationalError as e:
        print("erro ao criar tabelas: " + str(e))

print("TESTANTO")