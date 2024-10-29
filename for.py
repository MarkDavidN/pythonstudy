fruits=["banana","mangoes","pineapple","apple"]
for fruit in fruits:
    print(fruit)
    if fruit=="banana":

        print(fruit)

#range function=used to create a list of numbers fom acertain number to another
x=[1,2,3,4,7,8,9] 
y=list (range(9,100))  
print(y)         

#iterate through numbers from 20 to 100
c=list(range(20,101))
for num in c:
    print(num)
print(list(range(0,8)) )

#iterate through numbers from 20 to 100 and display even no
numbers=list(range(20,101))
evenno=[]
for i in numbers:
    if i%2==0:
        #print(i)
        evenno.append(i)
print(evenno)      
#break=used to stop the loop  