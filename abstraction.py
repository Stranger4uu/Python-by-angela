# hiding the Implementation details of class And only showing the essential feature to the user

class Car():
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car stated....")
    
car = Car()
car.start()