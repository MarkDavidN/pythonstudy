fruits=["mango","banana",100,30.7, False,True]
print(type(fruits))
print(fruits[1])
#modifying elements
fruits[1]="oranges"
print(fruits[1])

#list methods used to modifydata inside the list
#append=used to add elements at end of list
fruits.append("pineapples")
print(fruits)
#insert=add items to a specific index
fruits.insert(2,1000)
print(fruits)

#remove=used to remove first occurence of a specific element in cases where they have appeared similarly twice
#nb all methods=.method()
num=[10,20,30,40,10]
num.remove(10)
print(num)

#pop=it removes items of a specific index
num.pop(0)
print(num)

#list slicing
print(num[0:2])

#klength
print(len(num))

#check if element is inside a list
students=["maina","mark","peter"]
#in=used to check
print("peter" in students)

#concatenate list
list1=[1,2,3,4,8,9]
list2=[0,9,8,7]
sum=list1 +list2
print(sum)