#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
data1=int(input("enter data 1"))
data2=int(input("enter data 2"))
data3=int(input("enter data 3"))
# largest=max(data1,data2,data3)
# print(largest)
if data1>data2 and data1>data3:
    print(data1)
elif data2>data1 and data2>data3:
    print(data2) 
else:
    print(data3)       