class Supermercado:

    def __init__(self):
        self.inventario=[]
    
    def agregarInventario(self,producto):
        self.inventario.append(producto)
    
    def mostrarInventario(self):
        print(self.inventario)

    def editarProductoInventario(self,buscador):
        bandera=True
        for producto in self.inventario:
            if(producto['codigo']==buscador):
                bandera=True
                producto['precio']=250000
                print("Producto Editado con exito")
                break
            else:
                bandera=False
        if(not bandera):
            print("Producto no encontrado en el inventario")