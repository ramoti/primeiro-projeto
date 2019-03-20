from flask import Flask,render_template
app= Flask(__name__)

class Pessoa():
    def __init__(self,nome,idade,nascimento):
        self.nome=nome
        self.idade=idade
        self.nascimento=nascimento


@app.route("/")
def carai():
    return render_template("inicio.html")

@app.route("/addpessoa")
def caramba():
    return render_template("adicionarpessoa.html")

@app.route("/listapessoa")
def caramb():
    lista=[Pessoa("Piske",17,"12/09/2001"), Pessoa("Ravi",17,"16/07/2001")]
    return render_template("listarpessoa.html", So_cara_foda= lista)


app.run(debug=True)
