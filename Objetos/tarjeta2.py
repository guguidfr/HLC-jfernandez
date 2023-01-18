from tarjeta import Tarjeta

class TarjetaCredito(Tarjeta):
    def __init__(self, entidad, titular, numero, caducidad, cvv, credito):
        super().__init__(entidad, titular, numero, caducidad, cvv)
        self.credito = credito
    
    def pagar(self, cantidad):
        pass

