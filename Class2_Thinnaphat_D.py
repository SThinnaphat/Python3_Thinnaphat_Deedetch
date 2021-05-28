class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    def sayHello(self):
        print("HelloWorld")
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

pickup1 = PickUp()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

EstateCar1 = EstateCar()
EstateCar1.turnOnAirConditioner()