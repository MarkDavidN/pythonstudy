#function to calculate area of triangle
def triangleare():
    base=int(input("enter base"))
    height=int(input("enter height"))
    area=(base*height)/2
    print(area)
triangleare()    

#create a function that calculates area of a rectangle
def recarea():
    length=int(input("enter length"))
    width=int(input("width"))
    area=(width*length)
    return recarea
x=recarea()  
print(recarea) 

def arearec(leng,width):
    area=leng*width
    return arearec
arearec(20,30)  

def evenodd():
    number=int(input("enter no"))
    if number%2==0:
        return "even"
    else:
        return "odd"
evenodd()    
def evenod(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'
evenod(9)    

#write a program that takes in 4 inputs..print largest and numbers should not be the same

num1=int(input("enter no 1"))
num2=int(input("enter no 2"))
num3=int(input("enter no 3"))
num4=int(input("enter no 4"))
largest=max(num1,num2,num3,num4)
