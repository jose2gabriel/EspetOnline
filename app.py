from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuário e senha fixos para teste
USUARIO = "gabriel"
SENHA = "1234"

USUARIO2 = "biel"
SENHA2 = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    erro = ""
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario == USUARIO and senha == SENHA:
            return redirect(url_for("home"))
        else:
            erro = "Usuário ou senha incorretos"

        if usuario == USUARIO2 and senha == SENHA2:
            return redirect(url_for("admin"))
        else:
            erro = "Usuário ou senha incorretos"
            
    return render_template("login.html", erro=erro)

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():
     erro = ""
     
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)
