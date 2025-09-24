class BestPeers:

    def update_status(self, text):
        print(f"Status: {text}")


class GoogleChat:

    def update_status(self, text):
        print(f"Status: {text}")


def send_status(application, status):
    application.update_status(status)


bp = BestPeers()
gc = GoogleChat()

send_status(bp, "My status on Best Peers")
send_status(gc, "My status on Google Chat\n")

print("****************************************************************")
print("****************************************************************\n")


class CreditCard:

    def pay(self, amount):
        print(f"Payement done by Credit card of amount {amount}")


class DebitCard:

    def pay(self, amount):
        print(f"Payement done by Debit card of amount {amount}")


class Upi:

    def pay(self, amount):
        print(f"Payement done by UPI of amount {amount}")


def payment(mode, amount):
    mode.pay(amount)


credit_card = CreditCard()
debit_card = DebitCard()
upi = Upi()

for i in [credit_card, debit_card, upi]:
    i.pay(500)
