#one parent-->one child
class A:
    def ShowA(self):
        return "A class"

class B(A):
    def ShowB(self):
        return "B Class" 


B1 = B()
print(B1.ShowA())   #internally python converts A.ShowA(B1)-->thats why self required as parameter  
print(B1.ShowB())   #internally python converts B.ShowB(B1)-->thats why self required as parameter   
#---------------------------------------------------------------------------------------------------------------------------

#Multi-Level Inheritance
#Grandparent ? Parent ? Child

class GrandFather:
    def prop(self):
        return "Long face"

class Father(GrandFather):
    def prop1(self):
        return "Small teeth"

class Son(Father):
    def prop2(self):
        return "Large Eyes"

obj = Son()

print(obj.prop())
print(obj.prop1())
print(obj.prop2())

#---------------------------------------------------------------------------------------------------------------
#Multiple Inheritance
#One child inherits from multiple parents

class A1:
    def showA(self):
        return "A"

class B1:
    def showB(self):
        return "B"

class C1(A1, B1):
    pass

obj = C1()
print(obj.showA())
print(obj.showB())
#---------------------------------------------------------------------------------------------------------------------

#Hierarchical Inheritance
#One parent → Many children

class A2:
    def showA(self):
        return "A function"

class B2(A2):
    pass

class C2(A2):
    def Hirerachy(self):
        return "Its an Hirearchieal"

#obj1 = B2()
obj2 = C2()

print(obj2.showA())
print(obj2.showA())
print(obj2.Hirerachy())



