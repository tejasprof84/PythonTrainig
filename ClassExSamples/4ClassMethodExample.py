class EmployeeData:
    MinSalary = 100 #government given
    Name=""
    Salary=0

    def __init__(self,name,salary):
        self.Name=name
        self.Salary=salary

    def PrintEmpDetails(self):
        calucatedsalaray=0
        if self.Salary > self.MinSalary:
            calucatedsalaray = self.Salary
        else:
            calucatedsalaray = self.MinSalary
        print(f"name : {self.Name} salary {calucatedsalaray}")  

   
    @classmethod
    def SetNewMinSalary(cls,salary):
         cls.MinSalary = salary


e1 = EmployeeData("Ram", 150)
e2 = EmployeeData("Sham", 200)
e3 = EmployeeData("Mam", 85)

e1.PrintEmpDetails()
e2.PrintEmpDetails()
e3.PrintEmpDetails()

print("---------------------------------------------------\n")


#government oredered new min salary = 170
EmployeeData.SetNewMinSalary(170)

e1.PrintEmpDetails()
e2.PrintEmpDetails()
e3.PrintEmpDetails()






    