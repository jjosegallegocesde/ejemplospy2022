from Supermercado import Supermercado
from Producto import Producto

opcion=1
almacenesExito=Supermercado()

while(opcion!=0):
    
    opcion=int(input("digite una opcion: "))

    if(opcion==1):
        codigo=input("digite un codigo de producto: ")
        nombre=input("digite un nombre de producto: ")
        precio=int(input("digite un precio de producto: "))

        producto=Producto(codigo,nombre,precio)
        productoRegistado=producto.registrarProducto()
       
        almacenesExito.agregarInventario(productoRegistado)
        almacenesExito.mostrarInventario()
        

    