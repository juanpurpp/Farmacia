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

@app.route("/boleta.html")
def boleta():
	return render_template("boleta.html", contenido ="test")

@app.route("/editmedicamentos.html")
def med():
	return render_template("editmedicamentos.html", contenido ="test")

@app.route("/vercompras.html")
def vercompras():
	return render_template("vercompras.html", contenido ="test")

@app.route("/admin.html")
def admin():
	return render_template("admin.html", contenido ="test")

if __name__ == "__main__":
	app.run(debug=True)

