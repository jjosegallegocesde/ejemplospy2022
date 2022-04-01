class Producto:

    def __init__(self,codigo,nombre,precio):

        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
       

    def registrarProducto(self):

        producto={

            "codigo":self.codigo,
            "nombre":self.nombre,
            "precio":self.precio   
        }
        return producto
    
