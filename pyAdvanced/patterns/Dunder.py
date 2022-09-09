#Dunder
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print("object is deleted")

p = Person("Mike",25)
del p