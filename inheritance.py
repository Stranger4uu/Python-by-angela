class Car:
    @staticmethod
    def start():
        print("started...")

    @staticmethod
    def stop():
        print("stopped...")

class ToyatoCar (Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyatoCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Petrol")
print(car1.type)

car1 = ToyatoCar("Forturner")
car2 = ToyatoCar("prius")

print(car1.brand)
print(car2.brand)
print(car1.start())
print(car1.stop())


''' There are 3 types of inheritance
1. single inheritance
2. multi-level inheritance
3. multiple inheritance ( a class inheriting properties of multiple parent class or base class )
'''

class A:
    varA = "Welcome to class A..."

class B:
    varB = "Welcome to class B..."

class C(A, B):
    varC = "Welcome to class C..."

c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)
