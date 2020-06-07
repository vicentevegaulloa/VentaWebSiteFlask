from datetime import datetime
from flaskblog import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    fono = db.Column(db.String(15))
    celu_nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))

    def __repr__(self):
        return f"Cliente('{self.id}', '{self.nombre}')"

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    precio_unitario = db.Column(db.Integer)
    unidad = db.Column(db.Integer)
    costo_prov = db.Column(db.Integer)

    def __repr__(self):
        return f"Producto('{self.id}', '{self.nombre}')"

class Direccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String())
    calle = db.Column(db.String())
    numero_muni = db.Column(db.String())
    comuna = db.Column(db.String())
    unidad = db.Column(db.String())
    n_unidad = db.Column(db.String())


    def __repr__(self):
        return f"Direccion('{self.id}', '{self.calle}', '{self.comuna}')"

class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())


    def __repr__(self):
        return f"Estado('{self.id}', '{self.nombre}')"
