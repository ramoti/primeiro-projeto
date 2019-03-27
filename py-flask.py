from flask import Flask,render_template,request
app= Flask(__name__)

class Pessoa():
    def __init__(self,nome,idade,nascimento):
        self.nome=nome
        self.idade=idade
        self.nascimento=nascimento

lista=[Pessoa("Piske",17,"12/09/2001"), Pessoa("Ravi",17,"16/07/2001")]

@app.route("/")
def carai():
    return render_template("inicio.html")

@app.route("/addpessoa")
def caramba():
    return render_template("adicionarpessoa.html")

@app.route("/listapessoa_sem_add")
def caramb1():

    return render_template("listarpessoa.html", So_cara_foda= lista)

@app.route("/listapessoa")
def caramb2():

    nome= request.args.get("Nome")
    idade= request.args.get("Idade")
    nasci= request.args.get("Nascimento")
    lista.append(Pessoa(nome,int(idade),nasci))

    return caramb1()

@app.route("/deletepessoa")
def caramb3():

    nome= request.args.get("Nome")
    for pessoa in lista:
        if nome== pessoa.nome:
            lista.remove(pessoa)
            break
    return render_template("mensagem.html")


app.run(debug=True)

