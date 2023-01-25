import carrito
import productos
import cliente
import pago

camiseta_roja = productos.Ropa(nombre="Camiseta roja adidas", codigo="0000", precio=15, descripcion="Una camiseta roja de Adidas", talla="L", tejido="Algodón", color="Rojo")
jose_daniel = cliente.Cliente(nombre="José Daniel", correo="yo@correo.com", tlfno="123456789", direccion="Mi casa")
carrito1 = carrito.Carrito(jose_daniel)
carrito1.add_item(camiseta_roja)
jose_daniel.add_payment()
carrito1.show_items()
print(jose_daniel.metodos_pago)
carrito1.pagar_carrito()