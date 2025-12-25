class Animal:
	def sound(self):
		return "Animal make sounds"

class Dog(Animal):
	def sound(self): #method overided
		return "Dog barks"


animal = Animal()
dog = Dog()

print(animal.sound())
print(dog.sound()) #method overided


""" Animal has a method sound()

Dog overrides sound()

When sound() is called on a Dog object, Python uses the child’s method, not the parent’s
"""
"""Key Rules of Method Overriding

Method name must be same

Parameters must be same

Happens only in inheritance

Child method replaces parent method

Python decides the method at runtime (runtime polymorphism)

def: Method overriding is the process by which a child class redefines a parent class method to provide a specific implementation. 
i,e Same method name → different behavior.
"""