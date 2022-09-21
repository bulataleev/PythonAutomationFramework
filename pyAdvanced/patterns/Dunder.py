#Dunder
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print("object is deleted")

p = Person("Mike",25)
del p

class Vector:
    def __init__(self,x,y):
        self.x= x
        self.y= y
    def __add__(self,other):
        return Vector(self.x + other.x,
                    self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y is {self.y}"
    
    def __call__(self):
        print("the object was called")

v1 = Vector(1,2)
v2 = Vector(1,2)
v3= v1 + v2
print(v3)