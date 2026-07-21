class AlertService:
    def dispatch(self, text):
        print(f"Dispatching: {text}")

class AlertServiceWrapper(AlertService):
    def __init__(self, service):
        self.service = service
        
    def dispatch(self, text):
        self.service.dispatch(text)

class TextMessageWrapper(AlertServiceWrapper):
    def dispatch(self, text):
        super().dispatch(text)
        print("Additionally dispatching via Text Message")


if __name__ == "__main__":
    alert_system = TextMessageWrapper(AlertService())
    alert_system.dispatch("Greetings!")