num1=200
num2=300
mult=num1*num2
print(mult)

num="1000"
num=int(num)
num2="2000"
num2=int(num2)
print(num+num2)

#Questions
#Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57
#Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893 
#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 

#1Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57
temp=56.892
temp=round(temp)
print(temp)




#2Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
num=56.8927
print(round(num,2))


##Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
num=56.8927
#convert to astring first
num=str(num)
print(num)
num=num[3:]
print(num)
#concat8922
temp=num[0]+"."+num[1:]
print(temp)
temp=float(temp)
print(temp)



