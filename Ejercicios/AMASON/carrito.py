import cliente
import productos
import pago
class Carrito:
    def __init__(self, cliente):
        self.usuario = cliente
        self.items = []
        self.coste_productos = 0
        self.gasto_envio = self.coste_productos*0.06
        self.total = self.coste_productos + self.gasto_envio

    def add_item(self, producto):
        self.items.append(producto)
        print(f"Se ha añadido: {producto.nombre}")
        self.coste_productos += producto.precio

    def remove_item(self, producto):
        self.items.remove(producto)
        print(f"Se ha eliminado: {producto}")
        self.coste_productos -= producto.precio
    
    def show_items(self):
        print("Los elementos de tu carrito de la compra son:")
        contador = 0
        for item in self.items:
            contador += 1
            print(f"{contador}: {item.nombre}")
        print(f"El precio actual del carrito es: {self.coste_productos} (De coste de los productos) + {self.gasto_envio} (De gastos de envío) = {self.total}")
    
    def pagar_carrito(self):
        self.show_items()
        if len(self.usuario.metodos_pago) != 0:
            print("Puedes usar los diferentes métodos de pago:")
            for opciones in self.usuario.metodos_pago.keys():
                print(f"- {opciones}")
            metodo = str(input("Elige uno de los métodos de pago: "))
            if metodo in self.usuario.metodos_pago:
                self.usuario.metodos_pago[metodo].pagar(self.total)
            else:
                print(f"El método de pago \"{metodo}\" no está disponible.")
        else:
            print("No tienes ninún método de pago asociado a tu cuenta. Añade uno.")