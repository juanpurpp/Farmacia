from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")#Indica que será la pagina de inicio
def inicio():
	#return render_template("tema.html", contenido = nombre, otro ="otro nombre")
	return render_template("pagina.html", contenido = "Test")

if __name__ == "__main__":
	app.run(debug=True)