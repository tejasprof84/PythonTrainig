class Bird:
    def fly(self):
        print("Bird can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies fast")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")



birds = [Sparrow(), Penguin()]

for bird in birds:
    bird.fly()
    


    """
    The same method call behaves differently depending on the object type at runtime.

    Overriding is how you write it.
Polymorphism is how you use it.



Overriding creates polymorphism.
Polymorphism is the result you see at runtime.


"""