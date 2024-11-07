#define a class named car
class Car:
    def __init__(self,color,brand,shape) -> None:
        self.color=color
        self.brand=brand
        self.shape=shape
    def describe(self):
        return f'the color of this car is {self.color} and thre brand is {self.brand}.the shape is {self.shape}'    
mycar=Car("red",'bmw','wagon')
car1=Car('green','audi','sedan')
print(mycar.describe())   


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details (self):
        return f"hello my name is{self.name}and i am{self.age}years old"
mydetails=Student('mark',22)
print(mydetails.details())


class calculator():
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def substarct(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num1/self.num2
numbers = calculator(24,6)
print(numbers.divide())
print(numbers.substarct())
print(numbers.add())
print(numbers.multiply())


        