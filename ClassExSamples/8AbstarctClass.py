from abc import ABC, abstractmethod
class Vehicle(ABC):
   # @abstactmethod
    def start(self):
        pass
   


class Start_vehicle(Vehicle):
    def tayota(self):
        print("enter a button")
    def maruthi(self):
        print("Rotate a Key")


class model(Vehicle):
    def Seden():
        print("2012 Model")
    def HAtbatch():
        print("2023 model")


strvch = Start_vehicle()
mdl = model()

strvch.tayota()
strvch.maruthi()


