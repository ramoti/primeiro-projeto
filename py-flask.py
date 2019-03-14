from flask import Flask,render_template
app= Flask(__name__)

@app.route("/")
def carai():
    return render_template("inicio.html")

@app.route("/addpessoa")
def caramba():
    return render_template("adicionarpessoa.html")

@app.route("/listapessoa")
def caramb():
    return render_template("listarpessoa.html")


app.run(debug=True)
