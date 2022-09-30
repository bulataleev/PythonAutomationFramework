def mydecorator(function):
    def wrapper(*args, **kwargs):
        print("i am decorating ur function")
        function(*args,**kwargs) #return function(args,kwargs) if the implied method has return method
    return wrapper

@mydecorator
def hi_world(name):
    print(f"hi world {name}") #decorator must return func if this method is retirming

hi_world("Bulat")#already decorated

#mydecorator(hi_world)() #direct calling not used

#practical example - loggin
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args,**kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"{fname} returned value {value}")
        return value
    return wrapper

@logged
def add(a,b):
    return a+b

print(add(10,1))

