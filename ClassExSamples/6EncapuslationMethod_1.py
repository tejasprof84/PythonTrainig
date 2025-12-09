class Employee:
    
    def __init__(self,name,salary,password):
        self.Name=name  #Public
        self._Salary=salary  #protected
        self.__Password=password  #private attribute


    def show_employee_details(self):
        print("Salary " , self._Salary)
        print("Name ", self.Name)
        print("Password ",self.__Password)





Employees = Employee("Tej",25000,"Collpad121@")
print("use of methods to acess Private variable\n")
Employees.show_employee_details()  #private attributes can be acessed using methods

#acess each data in class
print("\n")
print("Name ",Employees.Name)
print("Salary ",Employees._Salary)
#print("Pasword ",Employees.__Password)  ->> It throw Attribute Error tell no attribute of __password is there bcs private varibale


#how to acess private variables in classs method
print("use of class Attribute Mangling method to acess Private variable")
print(Employees._Employee__Password) #its called  Python's name mangling for private variables


#Private variables are “hidden” by renaming them with:
#Obj._ClassName__variable
