class Engine:
	def start(self):
		print ("car has started")

class Car:
	def __init__(self):
		self.engine = Engine() #composition -->callin other class method inside another class

	def drive(self):
		self.engine.start()
		print("Car is moving")

car = Car()
car.drive()



