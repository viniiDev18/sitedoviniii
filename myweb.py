from flask import Flask, render_template, redirect, request

app = Flask(__name__)
# route => domínio do seu site, ex: /contatos, /homepage.
# função => o que você quer exibir naquela página.

# colocar o site no ar

@app.route("/")
def web():
    return redirect("/login")
    

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/dados", methods=["POST"])
def dados():
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    print(f"Usuário: {nome}")
    print(f"Senha: {senha}")
    if nome == "viniiz" and senha == "50028051a":
        return redirect("/usuarios")
    else:
        return redirect("/")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuarios") # <> => flask ler o nome de usuário
def usuarios(): 
    return render_template("usuarios.html") # retorna a variável descrita em html


if __name__ == "__main__":
    app.run(debug=True)

# colocar nosso site para pessoas acessarem
