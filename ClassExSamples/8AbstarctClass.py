from abc import ABC ,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self): #Abstract class = rule only
        pass
   


class Start_vehicle(Vehicle):
    def start(self):  #“Every vehicle must know how to start.” forcing start method to implement in every vehicle
        print("Push a button to start ")
    def tayota(self):
        print("enter a button")
    def maruthi(self):
        print("Rotate a Key")


class model(Vehicle):
    def start(self): #“Every vehicle must know how to start.”
        print("Rotate a key  to start ")
    def Seden(self):
        print("2012 Model")
    def HAtbatch(self):
        print("2023 model")


strvch = Start_vehicle()
mdl = model()

print(strvch.start())
print(mdl.start())

"""for method_name in dir(strvch):
    if not method_name.startswith("__"):
        method = getattr(strvch, method_name)
        if callable(method):
            method()
            """
"""Abstraction = define a rule in a base class, force child classes to implement it, and use the rule without caring about the details."""
    