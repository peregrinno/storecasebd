from flask import Flask, render_template, request

app = Flask(__name__)

#criar pagina
@app.route("/", methods=["GET", "POST"])
def homepage():
    variavel = "Cadastra na tabela produto"
    
    if request.method == "GET":
        return render_template("homepage.html", variavel=variavel)
    else:
        categoria = request.form.get("categoria_produto")
        tipo = request.form.get("tipo_produto")
        preco = request.form.get("preco")

        s_categoria = f'{categoria}'
        s_tipo  = f'{tipo}'
        s_preco = f'{preco}'
        return render_template("homepage.html", categoria=s_categoria,tipo=s_tipo,preco=s_preco)

#site online
if __name__ == "__main__":
    app.run(debug=True)
    
