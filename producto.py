class Producto:
    def __init__(self, nombre, precio, stock = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        
    # Obtener el nombre del producto
    @property
    def obtener_nombre(self):
        return self.__nombre
    
    # Obtener precio del producto
    @property
    def obtener_precio(self):
        return self.__precio
    
    # Obtener stock del producto
    @property
    def obtener_stock(self):
        return self.__stock
    
    # modificar el stock
    @obtener_stock.setter
    def modificar_stock(self, cantidad):
        if cantidad < 0:
            cantidad = 0
        self.__stock += cantidad
    