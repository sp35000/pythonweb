from flask import Flask, render_template

app = Flask(__name__)

# POSTS MOCK
posts = [
    {
        "titulo":"titulo 1",
        "texto":"post 1"
    },
    {
        "titulo":"titulo 2",
        "texto":"post 2"
    },
    {
        "titulo":"titulo 3",
        "texto":"post 3"
    }
]

@app.route("/")
def exibir_entradas():
    return render_template('exibir_entradas.html',entradas=posts)