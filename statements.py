marks=int (input("enter marks"))
if marks>=90:print("A")
elif marks>=80 and marks<90:print("B")
else : print("fail")

#write a program that takes age from input
#age above 18=adult
#age below 18=minor

age= int (input("enter age"))
if age>=18 :
    print("adult")
elif age <=18 :
     print("minor")
else:print("invalid")


#nested if statements
#give 100 discount on purchase above 1000
#200 discount on purchase above 7000
#no discount
purchase=int(input("enter price"))
if purchase>1000 and purchase<7000:
     print("100 discount")
     if purchase>7000:print("200 discount")
else: print ("no discount") 

#write a program that takes users age as input
#18 and above,check if they have drivers license,if the do prinmt'eligible to drive" if they dont"not eligible
#below 18 not eligible to drive

age=int(input("enter age"))
if age>=18:
     license=input("do you have a license yes/no")
     if license=="yes":
          print("you are eligible to drive")
     else :
          print("you are not eligible to drive")

else:
     print("you are not eligible to drive89")
#write a program that:
#Write a program that:
#Takes the user's credit score and annual income as input.
#=>If the credit score is above 700, check if the income is above $50,000:
#If both conditions are met, print "Loan approved."
#If only the credit score is high, print "Income requirement not met."
#=>If the credit score is below 700, print "Credit score too low."
creditscore=int(input("enter credit score"))
income=int(input("enter income"))
if creditscore>700:
     if income>70000:print("loan approved")
     else:print("income requirement not met")
else:print("credit score too low")     

    
