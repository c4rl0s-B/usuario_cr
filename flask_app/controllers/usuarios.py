from flask_app import app #Importamos la app

from flask import render_template, redirect, request, url_for
from flask_app.models.usuario import Usuario

@app.route("/") 
def inicio():
    return redirect(url_for("usuarios"))

@app.route("/usuarios")
def usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("nuevo_usuario.html")

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.save(data)
    return redirect(url_for("usuarios"))