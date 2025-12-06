class StudentWthutConstructor:
    name=str
    location=str
    age=int
   
'''student2=StudentWthutConstructor()
student2.name=input("enter name : ")
student2.location=input("enter location : ")
student2.age=int(input("enter age : "))
print(f"name : {student2.name},location : {student2.location},age : {student2.age}")'''
#----------------------------------------------------------------------------------------------------

class StudentWithConstructor:
    def __init__(self, nameparam : str, ageparam : str):  
        self.name = nameparam + " kumar"
        self.age = ageparam
        print(f"name : {nameparam}, age : {ageparam}")  ##here o/p is name and age "no kumar" is concatenated because its calling parameter

stu = StudentWithConstructor(input(" Enter the name `"),input(" Enter age "))
print(f"name : {stu.name}, age : {stu.age}") # here o/p is name + "kumar" and age bcs its taking entire name