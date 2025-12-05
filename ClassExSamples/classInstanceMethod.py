class Student:
    # constructor to create instance variables
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age        # instance variable
    
    # instance method
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

    
    def GetSummary(self):
        print(f"Student Name: {self.name}, Age: {self.age}")



# creating objects (instances)
s1 = Student("Rahul", 20)
s2 = Student("Priya", 19)

# calling instance methods
s1.show_details()
s2.show_details()

s1.GetSummary()
s2.GetSummary()
