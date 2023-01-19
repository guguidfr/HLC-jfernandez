class MetodoPago:
    def __init__(self, moneda, saldo_asociado):
        self.moneda = moneda
        self.saldo_asociado = saldo_asociado
    
    def pagar(self):
        pass

class PayPal(MetodoPago):
    def __init__(self, moneda, saldo_asociado, usuario_pp, region):
        super().__init__(moneda, saldo_asociado)
        self.usuario_pp = usuario_pp
        self.region = region

    def __str__(self):
        return f"El usuario es '{self.usuario_pp}', su moneda es '{self.moneda}' y su región es '{self.region}'."
    
class Bisum(MetodoPago):
    def __init__(self, moneda, saldo_asociado, tlfn, banco):
        super().__init__(moneda, saldo_asociado)
        self.tlfn = tlfn
        self.banco = banco
    
    def __str__(self):
        return f"El número de teléfono '{self.tlfn}' es el asociado para realizar el bisum."

class TarjetaDebito(MetodoPago):
    def __init__(self, moneda, saldo_asociado, titular, numero, cvv, fecha_cad, banco):
        super().__init__(moneda, saldo_asociado)
        self.titular = titular
        self.numero = numero
        self.cvv = cvv
        self.fecha_cad = fecha_cad
        self.entidad = banco

class TarjCredito(TarjetaDebito):
    def __init__(self, moneda, saldo_asociado, titular, numero, cvv, fecha_cad, banco, credito = 150):
        super().__init__(moneda, saldo_asociado, titular, numero, cvv, fecha_cad, banco)
        self.credito = credito
        self.fondos_disponibles = self.credito + self.saldo_asociado
