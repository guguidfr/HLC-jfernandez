import cliente
import productos
import pago
class Carrito:
    def __init__(self, cliente):
        self.usuario = cliente
        self.items = []
        self.coste = 0

    def add_item(self, producto):
        self.items.append(producto)
        print(f"Se ha añadido: {producto.nombre}")
        self.coste += producto.precio

    def remove_item(self, producto):
        self.items.remove(producto)
        print(f"Se ha eliminado: {producto}")
        self.coste -= producto.precio
    
    def show_items(self):
        print("Los elementos de tu carrito de la compra son:")
        contador = 0
        for item in self.items:
            contador += 1
            print(f"{contador}: {item.nombre}")
    
    def pagar_carrito(self):
        '''
        total = 0
        for item in self.items:
            total += self.items[item.precio]
        print(f"El precio total del carrito es: {total}")
        '''
        if len(self.usuario.metodos_pago) != 0:
            print("Puedes usar los diferentes métodos de pago:")
            for opciones in self.usuario.metodos_pago.keys():
                print(f"- {opciones}")
            metodo = input("Elige uno de los métodos de pago: ")
            if metodo in self.usuario.metodos_pago:
                self.usuario.metodos_pago[f"{metodo}"].pagar(self.coste)
            else:
                print(f"El método de pago \"{metodo}\" no está disponible.")
        else:
            print("No tienes ninún método de pago asociado a tu cuenta. Añade uno.")