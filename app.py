from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuário e senha fixos para teste
USUARIO = "gabriel"
SENHA = "1234"

USUARIO2 = "biel"
SENHA2 = "1234"

#armazena os informaçoes de login dos garçons
garcons = {}

@app.route("/", methods=["GET", "POST"])
def login():
    erro = ""
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        #login de usuario
        if usuario == USUARIO and senha == SENHA:
            return redirect(url_for("home"))
        else:
            erro = "Usuário ou senha incorretos"
        #login de admin
        if usuario == USUARIO2 and senha == SENHA2:
            return redirect(url_for("admin"))
        else:
            erro = "Usuário ou senha incorretos"
        #login de garçon
        if usuario in garcons and senha == garcons[usuario]["senha"]:
            return redirect(url_for("garcom"))

        erro = "Usuário ou senha incorretos"

    return render_template("login.html", erro=erro)

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    erro = ""
    msg = ""
    if request.method == "POST":
        # cria um login para o garçon
        novo_user = request.form.get("novo_usuario")
        nova_senha = request.form.get("nova_senha")

        if novo_user in garcons:
            erro = "Esse garçom já existe!"
        else:
            garcons[novo_user] = {"senha": nova_senha}
            msg = f"Garçom {novo_user} criado com sucesso!"
    return render_template("admin.html", erro=erro, msg=msg, garcons=garcons)

@app.route("/garcom")
def garcom():
    return render_template("garcom.html")


if __name__ == "__main__":
    app.run(debug=True)
