class Carrito:
    def __init__(self, cliente):
        self.usuario = cliente.nombre
        self.items = []

    def add_item(self, producto):
        self.items.append(producto)

    def remove_item(self, producto):
        self.items.remove(producto)
    
    def show_items(self):
        print("Los elementos de tu carrito de la compra son:")
        contador = 0
        for item in self.items:
            contador += 1
            print(f"{contador}: {item.nombre}")
    
    def pagar_carrito(self, cliente):
        if len(cliente.opciones_pago) != 0:
            print("Puedes usar los diferentes métodos de pago:")
            for opciones in cliente.opciones_pago:
                print(f"- {opciones}")
                
        else:
            print("No tienes ninún método de pago asociado a tu cuenta. Añade uno.")