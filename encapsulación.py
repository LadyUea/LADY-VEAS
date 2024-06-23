class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto

    def obtener_saldo(self):
        return self.__saldo

# Uso de la clase
cuenta = CuentaBancaria(100)
cuenta.depositar(50)
cuenta.retirar(30)
print(cuenta.obtener_saldo())  # Output: 120