class Coche:
    # Cosas que todos los objetos tengan en común, los ponemos directmente dentro de la clase
    # Atributos de clase
    ruedas = 4
    # Cosas que puedan ser diferentes entre los objetos, se ponen dentro de init
    def __init__(self, marca, modelo, color, motor, precio, combustible):
        # Atributos de objeto
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.precio = precio
        self.combustible = combustible
    
    def __str__(self):
        return(f"Es un coche {self.marca} modelo {self.modelo} de color {self.color} que tiene un motor {self.motor}, su precio es de {self.precio} y usa {self.combustible} como combustible.")

    def arranca(self):
        print("Brum, brum")
    
    def frena(self):
        print("Wiiiii")
    
    def choca(self, otro_coche):
        print("¡Pum!")
        print(f"Un {self.marca} ha chocado con un {otro_coche.marca}.")
# ------------------------------------------------------------------------
coche1 = Coche("Fiat","Punto","Azul","1600TDI", "6000€", "Diésel")
coche2 = Coche("Peugeot","206","Rojo","1200TDI", "3000€", "Gasolina")
print("Arrancamos el coche1")
coche1.arranca()
print("Arrancamos el coche2")
coche2.arranca()
print("Coche1 frena")
coche1.frena()
print("Los coches se estrellan")
coche1.choca(coche2)
# ----------------------------
print(coche1)
print(coche2)

coche1.fecha_itv="15/06/2023" #type: ignore
print(coche1.fecha_itv) #type: ignore
# ------------------------------------------------------------------------
class CocheElectrico(Coche):
    def __init__(self, marca, modelo, color, motor, precio, combustible, autonomia):
        super().__init__(marca, modelo, color, motor, precio, combustible)
        self.autonomia = autonomia
    
    def arranca(self):
        print("ZZZzZZzzzzzZzzzzzZ...")

mi_tesla = CocheElectrico("Tesla", "S", "Blanco", "Tesla 1", "104000€", "Eléctrico", "400Km")
mi_tesla.arranca()
# ------------------------------------------------------------------------
class Taller:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coches_averiados = []
    
    def reparar_coche(self, coche):
        print(f"Recibido el coche {coche.marca} para reparar.")
        self.coches_averiados = self.coches_averiados.append(coche) #type: ignore

taller_ciudad_jardin = Taller("Talleres CJ S.L")
taller_ciudad_jardin.reparar_coche(mi_tesla)