import cliente
class MetodoPago:
    def __init__(self, nombre, moneda,saldo_asociado = 0):
        self.nombre = nombre
        self.moneda = moneda
        self.saldo_asociado = saldo_asociado

    '''    
    def __str__(self):
        return self.nombre
    '''
    def pagar(self, cantidad):
        if self.saldo_asociado != 0 and self.saldo_asociado >= cantidad:
            self.saldo_asociado -= cantidad
            print(f"Se han restado {cantidad} {self.moneda}."       )
            print(f"Quedan {self.saldo_asociado} {self.moneda} en {self.nombre}.")
        else:
            print(f"\"{self}\" no cuenta con fondos suficientes para pagar el carrito.")

class PayPal(MetodoPago):
    def __init__(self, nombre, moneda, saldo_asociado, usuario_pp, region):
        super().__init__(nombre, moneda, saldo_asociado)
        self.usuario_pp = usuario_pp
        self.region = region

    def __str__(self):
        return f"El usuario es '{self.usuario_pp}', su moneda es '{self.moneda}' y su región es '{self.region}'."

    

class Bisum(MetodoPago):
    def __init__(self, nombre, moneda, saldo_asociado, tlfn, banco):
        super().__init__(nombre, moneda, saldo_asociado)
        self.tlfn = tlfn
        self.banco = banco
    

    def __str__(self):
        return f"El número de teléfono '{self.tlfn}' es el asociado para realizar el bisum."
    

class TarjetaDebito(MetodoPago):
    def __init__(self, nombre, moneda, saldo_asociado, titular, numero, cvv, fecha_cad, banco):
        super().__init__(nombre, moneda, saldo_asociado)
        self.titular = titular
        self.numero = numero
        self.cvv = cvv
        self.fecha_cad = fecha_cad
        self.entidad = banco

class TarjetaCredito(TarjetaDebito):
    def __init__(self, nombre, moneda, saldo_asociado, titular, numero, cvv, fecha_cad, banco, credito = 150):
        super().__init__(nombre, moneda, saldo_asociado, titular, numero, cvv, fecha_cad, banco)
        self.credito = credito
        self.fondos_disponibles = float(self.credito + self.saldo_asociado)

    def pagar(self, cantidad):
        if self.fondos_disponibles != 0 and self.fondos_disponibles >= cantidad:
            self.fondos_disponibles -= cantidad
            print(f"Se han restado {cantidad} {self.moneda}.")
            print(f"Quedan {self.fondos_disponibles} {self.moneda} en {self.nombre}.")
        else:
            print(f"\"{self}\" no cuenta con fondos suficientes para pagar el carrito.")