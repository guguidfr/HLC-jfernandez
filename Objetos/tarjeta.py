class Tarjeta: # "Plantilla para crear objetos."
    # Atributos:
    '''
    ancho=5
    alto=3
    '''
    
    # Constructor: -- Inicializar el objeto
    def __init__(self, entidad, titular, numero, caducidad, cvv):
        # Atributos de la instancia (del objeto)
        self.entidad=entidad
        self.titular=titular
        self.numero=numero
        self.caducidad=caducidad
        self.cvv=cvv
        self.activacion = False
        self.saldo = 0

    # Métodos:
    def activar(self):
        if self.activacion:
            print(f"La tarjeta con número {self.numero} ya estaba activada.")
        else:
            self.activacion = True
            print(f"Activando la tarjeta con número {self.numero}.")
    
    def pagar(self, cantidad):
        if self.activacion:
            print(f"Pagando {cantidad}€ con la tarjeta {self.numero}.")
        else:
            print(f"No se puede pagar porque la tarjeta con número {self.numero} porqué está anulada")

    def anular(self):
        if not self.activar:
            self.activacion = False
            print(f"Anulando la tarjeta con número {self.numero}.")
        else:
            print(f"La tarjeta con número {self.numero} ya estaba anulada.")

    def recargar(self, importe):
        self.saldo+=importe
        print(f"Se han añadido {importe}€ a la tarjeta {self.numero}")

# Instanciar una clase, a.k.a crear un objeto:
tarjeta1=Tarjeta("BBVA", "José Daniel", "1234123412341234", "12/24", 777)
tarjeta2=Tarjeta("ING", "Perro sanxe", "4321432143214321", "11/25", 111)
print(f"Tipo de la tarjeta1: {type(tarjeta1)}")
# ----------------------------------------------------------------------------
