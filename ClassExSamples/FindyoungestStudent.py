class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''
s1 = student(input("Name "), input("Age "))
s2 = student(input("Name "), input("Age "))
s3 = student(input("Name "), input("Age "))
s4 = student(input("Name "), input("Age "))
'''

studentList=[]

num=int(input("Enter number of students "))

for students in range(num):
    namein = input("Enter name ")
    agein = int(input("Enter age "))
    s = student(namein, agein)
    studentList.append(s)
    
'''for index, studentObject in enumerate(studentList):
    print(f"Index: {index}, Name: {studentObject.name}, Age: {studentObject.age}")'''
    
minAge=100000
minName=" "

for stu in studentList:
    print(f" Name: {stu.name}, Age: {stu.age}")
    if stu.age<minAge:
        minAge = stu.age
        minName = stu.name

print(f"The youngest student is {minName} with age {minAge}")


# for i in range(len(studentList)):
#     print(f"Index: {i}, Name: {studentList[i].name}, Age: {studentList[i].age}")

    