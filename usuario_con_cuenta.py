class Usuario:
    def __init__(self, nombre,cuenta):
        self.nombre = nombre
        self.cuenta = cuenta
    def hacer_deposito(self, amount):
            self.cuenta.hacer_deposito(amount)
            print(f"Se hizo un deposito de {amount} .")
    def hacer_retiro(self, cantidad) :
        if cantidad <= self.cuenta.balance:
            self.cuenta.hacer_retiro(cantidad)
            print(f"Se retiró la suma de {cantidad}.")
        else:
            print("Fondos insuficientes. No se pudo realizar el retiro.")
    def mostrar_balance_usuario(self):
                print(f"{self.nombre}, Saldo actual de : {self.cuenta}")
usu1 = Usuario("usuario",100)
class cuenta():
    def __init__(self, nombre,saldo_inicial = 0):
        self.nombre = nombre
        self.saldo = saldo_inicial
    def hacer_deposito(self, amount):
            self.saldo += amount
            print(f"Se hizo un deposito de {amount} .")
    def hacer_retiro(self, cantidad) :
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se retiro la suma de  {cantidad} .")
            else:
                print("Fondos insuficientes. No se pudo realizar el retiro.")
    def mostrar_balance_usuario(self):
                print(f"Saldo actual de {self.nombre}: {self.saldo}")