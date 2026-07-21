class CardTransaction:
    def execute(self, val):
        print("Paid Rs.", val, "using Credit Card")


class DigitalWalletTransaction:
    def execute(self, val):
        print("Paid Rs.", val, "using PayPal")


class TransactionContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, val):
        self.strategy.execute(val)


if __name__ == "__main__":
    context = TransactionContext(CardTransaction())
    context.process(1000)
    
    context = TransactionContext(DigitalWalletTransaction())
    context.process(2000)