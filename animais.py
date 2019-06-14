import os
from peewee import *

db = SqliteDatabase('animalia.db')

class Animal (Model):
    
    nomedono =CharField()
    tipo_animal =CharField()
    raca =CharField()
    
    class Meta:
        
        database = db
    
    def __str__(self):
        return self.tipo_animal+","+self.raca+" de "+self.nomedono

class Cliente (Model):
    nome =CharField()
    email =CharField()
    telefone =CharField()
    nome_login =CharField()
    senha =CharField()

    class Meta:

        database = db

    def __str__(self):
        return self.nome+", "+self.email+" - "+self.telefone+\
            " | "+self.nome_login+"/"+self.senha

class Consulta (Model):
    data =CharField()
    servico =CharField()
    horario =CharField()
    animal =ForeignKeyField(Animal)
    cliente =ForeignKeyField(Cliente)
    confirma =CharField()
    myID =CharField()

    class Meta:

        database = db

    def __str__(self):
        
        return self.servico+" em "+self.data+":"+self.horario+", confirmado: "+\
        self.confirma+", ID da consulta: "+self.myID+\
            " | animal: "+str(self.animal)+" | cliente: "+str(self.cliente)


if __name__ == '__main__':

    arq = 'animalia.db'
    if os.path.exists(arq):
        os.remove(arq)

    try:
        
        db.connect()
        db.create_tables([Animal,Consulta,Cliente]) 

    except OperationalError as e:
        print("erro ao criar tabelas: "+str(e))

    print("TESTE DO ANIMAL")
    a1 = Animal(nomedono="José", tipo_animal="C", raca="Chiuaua")
    print(a1)

    print("TESTE DO CLIENTE")
    jose = Cliente(nome="José", email="jose@gmail.com", telefone="47 99200-1010",
        nome_login="josesoueu", senha="123deoliveira4")
    print(jose)

    print("TESTE DA CONSULTA")
    
    c1 = Consulta(data="19/09/2018", servico="Consulta de rotina", 
        horario="14:00", animal=a1, cliente=jose, confirma="N", 
        myID="c9d8f7gu4h3hnwsik3e")
    print(c1)

    print("TESTE DA PERSISTÊNCIA")
    
    a1.save()
    
    jose.save()
    
    c1.save()
    
    c2 = Consulta(data="21/09/2018", servico="Aplicação de vacina", 
        horario="10:00", animal=a1, cliente=jose, 
        confirma="S", myID="d9firtu3434uit")
    
    c2.save()
    
    todos = Consulta.select()
    
    for con in todos:
        print(con)    