class iOSApp:
    def refresh(self, value):
        print("Mobile App Updated:", value)

class WebPortal:
    def refresh(self, value):
        print("Web App Updated:", value)

class ExchangeMarket:
    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def broadcast(self, value):
        for listener in self.listeners:
            listener.refresh(value)

if __name__ == "__main__":
    exchange = ExchangeMarket()
    
    phone_app = iOSApp()
    portal = WebPortal()
    
    exchange.subscribe(phone_app)
    exchange.subscribe(portal)
    
    exchange.broadcast(2500)