class LegacyPaymentSystem:
    def execute_transaction(self, val):
        print(f"Transaction of INR {val} successfully completed")


class PaymentSystemAdapter:
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def handle_payment(self, val):
        self.legacy_system.execute_transaction(val)


if __name__ == "__main__":
    old_system = LegacyPaymentSystem()
    system_adapter = PaymentSystemAdapter(old_system)
    
    system_adapter.handle_payment(8000)