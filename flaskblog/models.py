from datetime import datetime
from flaskblog import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    fono = db.Column(db.String(15))
    celu_nombre = db.Column(db.String(50))
    direccion = db.relationship("Direccion", uselist=False, back_populates="cliente")
    ventas = db.relationship("Venta", back_populates = "cliente")
    def __repr__(self):
        return f"Cliente('{self.id}', '{self.nombre}')"

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    precio_unitario = db.Column(db.Integer)
    unidad = db.Column(db.Integer)
    costo_prov = db.Column(db.Integer)
    # ventas = db.relationship("VentaProducto", back_populates="producto")

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
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    cliente = db.relationship("Cliente", back_populates="direccion")

    def __repr__(self):
        return f"Direccion('{self.id}', '{self.calle}', '{self.comuna}')"

class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    #ventas = db.relationship("VentaEstado", back_populates="estado")

    def __repr__(self):
        return f"Estado('{self.id}', '{self.nombre}')"
#
class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    cliente = db.relationship("Cliente", back_populates="ventas")
    # productos = db.relationship("VentaProducto", back_populates="venta")
    # estados = db.relationship("VentaEstado", back_populates="venta")

    def __repr__(self):
        return f"Venta('{self.id}')"
#
# class VentaProducto(db.Model):
#     venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), primary_key=True)
#     producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), primary_key=True)
#     cantidad = db.Column(db.Integer)
#     venta = db.relationship("Venta", back_populates="producto")
#     producto = db.relationship("Producto", back_populates="venta")
#
#     def __repr__(self):
#         return f"Venta('{self.venta_id}') y Producto('{self.producto_id}')"
#
# class VentaEstado(db.Model):
#     venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), primary_key=True)
#     estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'), primary_key=True)
#     fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
#     venta = db.relationship("Venta", back_populates="estado")
#     estado = db.relationship("Estado", back_populates="venta")
#
#     def __repr__(self):
#         return f"Venta('{self.venta_id}') y Producto('{self.estado_id}')"
