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

@app.route("/listapessoa")
def caramb():

    nome= request.args.get("Nome")
    idade= request.args.get("Idade")
    nasci= request.args.get("Nascimento")
    lista=[Pessoa("Piske",17,"12/09/2001"), Pessoa("Ravi",17,"16/07/2001")]
    lista.append(Pessoa(nome,int(idade),nasci))
    return render_template("listarpessoa.html", So_cara_foda= lista)


app.run(debug=True)
