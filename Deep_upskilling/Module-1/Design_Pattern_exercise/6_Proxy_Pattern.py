class Graphic:
    def render(self): pass

class HighResGraphic(Graphic):
    def render(self): print("Displaying high-res image")

class GraphicProxy(Graphic):
    def __init__(self):
        self._graphic_instance = None
        
    def render(self):
        if not self._graphic_instance:
            self._graphic_instance = HighResGraphic()
        self._graphic_instance.render()

if __name__ == "__main__":
    pic = GraphicProxy()
    pic.render()