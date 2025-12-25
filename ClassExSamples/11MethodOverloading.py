#method overloading using defaullt parameter
class calculator:
	def add(self, a,b=0,c=0):
		return  a+b+c


calc = calculator()
print(calc.add(2,3,4))	
print(calc.add(2))	
print(calc.add(2,7))	

print("---------------------------")
#method overloading using *args

class Caluculator:
	def sub(self,*args):
		sum = 0
		for num in  args:
			sum -=num

		return sum



calc1 = Caluculator()

print(calc1.sub(2,3,4))
print(calc1.sub(2,3,4,4,5,6))

print("--------------------------")

class Employee:
    def details(self, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

emp = Employee()
emp.details(name="Rahul", role="Developer", salary=50000)


"""Python achieves method overloading using default arguments, *args, and **kwargs instead of defining multiple methods with the same name.
"""
"""Method Overloading means:

Same method name, different number or type of parameters

Python supports this behavior, but not by defining multiple methods with the same name.
"""
