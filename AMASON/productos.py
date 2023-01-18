class ProductoGenerico:
    def __init__(self, nombre, codigo, precio, descripcion):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.descripcion = descripcion
    
    def __str__(self):
        return f"Nombre: {self.nombre} \nCódigo: {self.codigo} \nPrecio: {self.precio} \nDescripción: {self.descripcion}"
    
class Libro(ProductoGenerico):
    def __init__(self, nombre, codigo, precio, descripcion, isbn, autor, genero, editorial):
        super().__init__(nombre, codigo, precio, descripcion)
        self.isbn = isbn
        self.autor = autor
        self.genero = genero
        self.editorial = editorial

class Videojuego(ProductoGenerico):
    def __init__(self, nombre, codigo, precio, descripcion, plataforma, desarrolladora, pegi):
        super().__init__(nombre, codigo, precio, descripcion)
        self.plataforma = plataforma
        self.desarrolladora = desarrolladora
        self.pegi = pegi

class Mueble(ProductoGenerico):
    def __init__(self, nombre, codigo, precio, descripcion, dimensiones, material):
        super().__init__(nombre, codigo, precio, descripcion)
        self.dimensiones = dimensiones
        self.material = material

class Ropa(ProductoGenerico):
    def __init__(self, nombre, codigo, precio, descripcion, talla, tejido, color):
        super().__init__(nombre, codigo, precio, descripcion)
        self.talla = talla
        self.tejido = tejido
        self.color = color
        
        