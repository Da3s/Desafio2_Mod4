from tienda import Restaurante, Supermercado, Farmacia, Producto

def main():
    # Se crea la tienda
    nombre_tienda = input("Ingresa el nombre que deseas para la tienda: ")
    delivery = float(input("Ingresa el valor del delivery: "))
    tienda = 
    
    
    
    
    
    
    # Ingresar productos a la tienda
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        stock_producto = int(input("Ingrese el stock del producto: "))
        producto = Producto(nombre_producto, precio_producto, stock_producto)
        tienda.ingresar_producto(producto)
        continuar = input("¿Desea ingresar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break

    # Interacción con la tienda
    while True:
        print("\nSeleccione una opción:")
        print("1. Listar productos existentes")
        print("2. Realizar una venta")
        print("3. Salir del programa")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            print(tienda.listar_productos())
        elif opcion == '2':
            # Lógica para realizar venta
            pass
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()