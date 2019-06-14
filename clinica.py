import os
from peewee import *

arq = 'many-to-many-com-lista.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db
        
class Aluno(BaseModel):
    nome = CharField()

class Disciplina(BaseModel):
    nome = CharField()
    alunos = ManyToManyField(Aluno) 


if os.path.exists(arq):
        os.remove(arq)

db.connect()
db.create_tables([
    Aluno,
    Disciplina,
    Disciplina.alunos.get_through_model()])


joao = Aluno.create(nome = "Joao da Silva")
ingles = Disciplina.create(nome = 'Inglês')
espanhol = Disciplina.create(nome = 'Espanhol')

joao.disciplinas.add([ingles, espanhol])

maria = Aluno.create(nome = 'Maria')
espanhol.alunos.add(maria)

todos = Disciplina.select()
for disc in todos:
    print("Quem cursa a disciplina:"+disc.nome)
    for aluno in disc.alunos:
         print(aluno.nome)

print("Disciplinas de Joao:")
for disciplina in joao.disciplinas:
    print(disciplina.nome)