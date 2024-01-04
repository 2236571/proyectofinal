#Libreria para el uso de Flask
from flask import Flask, render_template

#libreria para el uso de la base de datos 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column  

app = Flask(__name__)
#configuro parametro SQLALCHEMY_DATABASE_URI con la ubicacion de la BD
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.sqlite"

db = SQLAlchemy(app)

#crear la tabla
class Todo(db.Model):
    id:Mapped[int]=mapped_column(db.Integer,primary_key=True,autoincrement=True)
    name: Mapped[str]=mapped_column(db.String,nullable=False)
    state: Mapped[str]=mapped_column(db.String,nullable=False,default='Incompleto')

#crea la base y las tablas necesarias con el contexto de la aplicacion
with app.app_context():
    db.create_all()

#rutas
@app.route("/",methods=['get','post'])
def home():
    if 
    return render_template("select.html") 

@app.route("/insert")
def insert(): 
    return'hola esto es una prueba de insertar de modificar'


@app.route("/update/<id>")
def update(id):
    return f'hola esto es una prueba para modificar el id {id}'


@app.route("/delete/<id>")
def delete(id):
    return f'hola esto es una pruebapara elimimar en id {id}'

if __name__ == '__main__':
    app.run(debug=True)