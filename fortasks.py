#Write a program that displays a numbers 1 to 50 inside a list.
# From 1 above display the ones divisible by 7 or 5 inside a list.
# Find sum and average of values in the range between 10 to 40.
# Put in a list the first 10 odd numbers between 10 to 50. 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.

#Write a program that displays a numbers 1 to 50 inside a list.
numlist=list(range(1,51))
print(numlist)

# From 1 above display the ones divisible by 7 or 5 inside a list.
numlist=list(range(1,51))
divby7orfive=[]
for i in numlist:
    if i%7==0 or i%5==0:
       # print(i)
       divby7orfive.append(i)
print(divby7orfive)       

# Find sum and average of values in the range between 10 to 40.
num=list(range(10,41))
#totalsum=sum(num)
#print(totalsum)
sum=0
for i in num:
   # print(i)
   sum+=i
   #sum=sum+i
print(sum)   
average=sum/len(num)
print(average)



# Put in a list the first 10 odd numbers between 10 to 50.
x=list(range(10,51)) 
oddno=[]
count=0
for m in x:
   if m%2!=0:
      oddno.append(m) 
      count+=1
      if count==10:
         break

print(oddno)      


# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number=int(input("enter number"))
for i in range(11):
   mult=number*i
   print(f'{number}*{i}={mult}')




# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
count=0
for i in range(1,51):
   if i%2==0:
      count+=1
print(count)       


# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.
totalquantity=0
ls1 = [ ('Jay', 20), ('Mo', 30), ('Mya', 32) ]
for l in ls1:
   stock=l[1]
   totalquantity+=stock
print(totalquantity)   