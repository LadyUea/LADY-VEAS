# Definición de la clase base BankAccount
class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder  # Atributo encapsulado
        self._balance = balance  # Atributo encapsulado

    # Método getter para obtener el titular de la cuenta
    def get_account_holder(self):
        return self._account_holder

    # Método getter para obtener el balance de la cuenta
    def get_balance(self):
        return self._balance

    # Método para depositar dinero en la cuenta
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance is ${self._balance}.")
        else:
            print("Deposit amount must be positive.")

    # Método para retirar dinero de la cuenta
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self._balance}.")
        else:
            print("Withdrawal amount must be positive and no more than the balance.")

    # Método que muestra información de la cuenta
    def display_info(self):
        print(f"Account Holder: {self._account_holder}, Balance: ${self._balance}")


# Definición de la clase derivada SavingsAccount que hereda de BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)  # Llamada al constructor de la clase base
        self._interest_rate = interest_rate  # Atributo específico de SavingsAccount

    # Método getter para obtener la tasa de interés
    def get_interest_rate(self):
        return self._interest_rate

    # Método para aplicar interés al balance
    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Applied ${interest} interest. New balance is ${self._balance}.")

    # Sobrescribir el método display_info para incluir la tasa de interés
    def display_info(self):
        print(
            f"Savings Account Holder: {self._account_holder}, Balance: ${self._balance}, Interest Rate: {self._interest_rate * 100}%")


# Definición de la clase derivada CheckingAccount que hereda de BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)  # Llamada al constructor de la clase base
        self._overdraft_limit = overdraft_limit  # Atributo específico de CheckingAccount

    # Método getter para obtener el límite de sobregiro
    def get_overdraft_limit(self):
        return self._overdraft_limit

    # Sobrescribir el método withdraw para incluir la funcionalidad de sobregiro
    def withdraw(self, amount):
        if 0 < amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self._balance}.")
        else:
            print("Withdrawal amount exceeds balance and overdraft limit.")

    # Sobrescribir el método display_info para incluir el límite de sobregiro
    def display_info(self):
        print(
            f"Checking Account Holder: {self._account_holder}, Balance: ${self._balance}, Overdraft Limit: ${self._overdraft_limit}")


# Ejemplo de uso de las clases y demostración de los conceptos de POO

# Creación de una instancia de la clase BankAccount
account = BankAccount("John Doe", 1000)
account.display_info()  # Salida: Account Holder: John Doe, Balance: $1000

# Realizar un depósito y una retirada
account.deposit(500)
account.withdraw(200)

# Creación de una instancia de la clase SavingsAccount
savings_account = SavingsAccount("Jane Doe", 2000, 0.05)
savings_account.display_info()  # Salida: Savings Account Holder: Jane Doe, Balance: $2000, Interest Rate: 5.0%

# Aplicar interés y mostrar la información actualizada
savings_account.apply_interest()
savings_account.display_info()  # Salida: Savings Account Holder: Jane Doe, Balance: $2100, Interest Rate: 5.0%

# Creación de una instancia de la clase CheckingAccount
checking_account = CheckingAccount("Alice Smith", 1500, 500)
checking_account.display_info()  # Salida: Checking Account Holder: Alice Smith, Balance: $1500, Overdraft Limit: $500

# Realizar una retirada con sobregiro y mostrar la información actualizada
checking_account.withdraw(1800)
checking_account.display_info()  # Salida: Checking Account Holder: Alice Smith, Balance: -$300, Overdraft Limit: $500
