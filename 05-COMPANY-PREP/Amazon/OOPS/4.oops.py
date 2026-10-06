class  Enginee:
    def start(self):
        print("engine started")
class car:
    def __init__(self):
        self.enginee=Enginee()
    def start_car(self):
        self.enginee.start()
car1=car()
car1.start_car()
