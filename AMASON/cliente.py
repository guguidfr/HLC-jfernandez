import pago as MetodosPago
class Cliente:
    def __init__(self, nombre, correo, tlfno, direccion):
        self.nombre = nombre
        self.correo = correo
        self.tlfno = tlfno
        self.direccion = direccion
        self.metodos_pago = {}
    
    def __str__(self):
        return self.nombre
    
    def add_payment(self):
        lista_pagos_disponibles = ("paypal", "bisum", "tarjetadedebito", "tarjetadecredito")
        n = int(input("¿Cuántos métodos de pago quieres añadir? "))
        for i in range(n):
            salir = False
            while salir == False:
                nombre_metodo = str(input(f"¿Cómo quieres llamar al método de pago {i+1}?: "))
                if " " in nombre_metodo:
                    print("No se admiten espacios en blanco en el nombre del método de pago.")
                else:
                    tipo = str(input("¿De qué tipo va a ser? PayPal, Bisum, TarjetaDeDebito, TarjetaDeCredito: ").lower())
                    if tipo not in lista_pagos_disponibles:
                        print("Ese método de pago no está entre las opciones.")
                    else:
                        salir = True
            
            if tipo == "paypal": #type: ignore
                self.metodos_pago[nombre_metodo] = MetodosPago.PayPal( #type: ignore
                    moneda = input("Introduce el tipo de moneda que usará tu cuenta de paypal: "),
                    saldo_asociado = int(input("Introduce el saldo de tu cuenta de PayPal: ")), 
                    usuario_pp = input("Introduce tu nombre de usuario de PayPal: "), 
                    region = input("Introduce la región de tu cuenta de PayPal: "))
            
            elif tipo == "bisum": #type: ignore
                self.metodos_pago[nombre_metodo] = MetodosPago.Bisum( #type: ignore
                    moneda = input("Introduce el tipo de moneda que usarás con Bisum: "),
                    saldo_asociado = int(input("Introduce el saldo que tienes en Bisum: ")), 
                    tlfn = input("Introduce el número de teléfono de tu Bisum: "), 
                    banco = input("Introduce el nombre de tu banco: ")) #type: ignore
            
            elif tipo == "tarjetadedebito": #type: ignore
                self.metodos_pago[nombre_metodo] = MetodosPago.TarjetaDebito( #type: ignore
                    moneda = input("Introduce la moneda de la tajeta de débito: "),
                    saldo_asociado = int(input("Introduce el saldo de la tarjeta de débito: ")), 
                    titular = input("Introduce el nombre de la persona titular de la tarjeta de débito: "), 
                    numero = input("Introduce el número de la tarjeta de débito: "), 
                    cvv = input("Introduce el CVV de la tarjeta de débito: "), 
                    fecha_cad = input("Introduce la fecha de caducidad de la tarjeta: "), 
                    banco = input("Introduce el nombre de tu banco: "))
            
            elif tipo == "tarjetadecredito": #type: ignore
                self.metodos_pago[nombre_metodo] = MetodosPago.TarjetaCredito( #type: ignore
                    moneda = input("Introduce la moneda de la tajeta de crédito: "),
                    saldo_asociado = int(input("Introduce el saldo de la tarjeta de crédito: ")), 
                    titular = input("Introduce el nombre de la persona titular de la tarjeta de crédito: "), 
                    numero = input("Introduce el número de la tarjeta de crédito: "), 
                    cvv = input("Introduce el CVV de la tarjeta de crédito: "), 
                    fecha_cad = input("Introduce la fecha de caducidad de la tarjeta: "), 
                    banco = input("Introduce el nombre de tu banco: "), 
                    credito = int(input("Introduce el crédito de la tarjeta: "))) #type: ignore