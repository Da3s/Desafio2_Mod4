from producto import Producto

class Tienda:
    def __init__(self, nombre, delivery):
        self.__nombre = nombre
        self.__productos = []
        self.__delivery = delivery
        
    def ingreso_productos(self, producto):
        for prod in self.__productos:
            if prod.obtener_nombre() == producto.obtener_nombre():
                prod.modificar_stock(producto.obtener_stock())
                return self.__productos.appen(producto)
            
    def listar_productos(self):
        productos = ""
        for prod in self.__productos:
            productos += f"Nombre: {prod.obtener_nombre()}, Precio: ${prod.obtener_precio()}\n"
            productos += self.info_adicional(prod)
        return productos
    
    def info_adicional(self, producto):
        return ""
    

class Supermercado(Tienda):
    def info_adicional(self, producto):
        if producto.obtener_stock() < 10:
            return "(Pocos productos disponibles)\n"
        return ""
    
    
class Farmacia(Tienda):
    def info_adicional(self, producto):
        if producto.obtener_precio() > 15000:
            return " (Envío gratis al solicitar este producto)\n"
        return ""
    
    
class Restaurante(Tienda):
    pass