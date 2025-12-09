#how to access Private Method
class Student:
    def __init__(self,name,id,password):
        self.Name = name
        self.Id = id
        self.Password = password

        #its private method __
    def __Student_details(self):
        print(self.Name)
        print( self.Id)
        print( self.Password)

stu = Student("Tej",25,"Collpad")
#stu.__Student_details() ---> it will raise an attribute erorr bcs cannt find __Student_details() method

#how to acess?
stu._Student__Student_details() #mangling topic to access privayr methods--> object._classname__method()
