#PROXY
class RealBankAccount:
    def __init__(self, balance):
        self.balance = balance

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Retiro: {amount}. Saldo restante: {self.balance}"
        return "Fondos insuficientes"

class BankAccountProxy:
    def __init__(self, real_account, authenticated=False):
        self.real_account = real_account
        self.authenticated = authenticated

    def authenticate(self):
        self.authenticated = True

    def retiro(self, amount):
        if not self.authenticated:
            return "Acceso denegado. Porfavor autentifiquese primero."
        return self.real_account.retiro(amount)


# Uso PROXY
real_account = RealBankAccount(1000)
proxy = BankAccountProxy(real_account)

print(proxy.retiro(100)) 
proxy.authenticate()
print(proxy.retiro(100)) 
print(proxy.retiro(100)) 
print(proxy.retiro(100)) 