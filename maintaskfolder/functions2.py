#Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
maths=int(input("enter marks of maths"))
eng=int(input("enter marks of eng"))
swa=int(input("enter marks of swa"))
sci=int(input("enter marks of sci"))
sos=int(input("enter marks of sos"))
def totalmarks(maths,eng,swa,sci,sos):

    total=maths+eng+ swa+sci+sos
    print(total)
totalmarks(maths,eng,swa,sci,sos)    
    

