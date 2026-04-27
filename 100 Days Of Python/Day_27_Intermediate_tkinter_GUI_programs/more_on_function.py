# Unlimited Positional Arguments.

def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)

add(2,2,2,2)

# Unlimited Keywords Arguments

def calculate(num,**kwargs):
    num += kwargs["add"]
    num -= kwargs["sub"]
    num *= kwargs["multiply"]

    return num

print(calculate(2,add=2 ,sub=5 ,multiply=2, divide = 2))

class Car:
    def __init__(self,**kwargs):
        self.model = kwargs["model"]
        self.seats = kwargs["seats"]
        self.tyres = kwargs.get("tyres") # .get() will return None if it's not passed


my_car = Car(model="Toyota",seats=2)
print(my_car.model,my_car.seats,my_car.tyres)