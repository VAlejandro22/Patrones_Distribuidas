#PATRON STRATEGY
# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete Strategy: Pago con tarjeta
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Pagado {amount} con tarjeta {self.card_number}"

# Concrete Strategy: Pago con PayPal
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Pagado {amount} con PayPal ({self.email})"

# Context
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item, price):
        self.items.append((item, price))
        self.total += price

    def pay(self, payment_strategy):
        return payment_strategy.pay(self.total)

# Uso STRATEGY
cart = ShoppingCart()
cart.add_item("Libro", 10)
cart.add_item("Camiseta", 20)

payment_method = CreditCardPayment("1234-5678-9012-3456")
print(cart.pay(payment_method))  # Output: Pagado 30 con tarjeta 1234-5678-9012-3456

paypal_method = PayPalPayment("user@example.com")
print(cart.pay(paypal_method))  # Output: Pagado 30 con PayPal (user@example.com)