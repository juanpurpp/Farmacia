from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("paginaprincipal.html", contenido = "Test")

@app.route("/comprar.html")
def comprar():
	return render_template("comprar.html", contenido ="test")

@app.route("/login.html")
def login():
	return render_template("login.html", contenido ="test")

if __name__ == "__main__":
	app.run(debug=True)

