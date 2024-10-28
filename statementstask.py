#Take three inputs from a user, separately. Print the largest of the numbers.
 #   Hint: Determine what type of data is taken in as input.
#Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
#4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
#5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

data1=float(input("enter data 1"))
data2=float(input("enter data 2"))
data3=float(input("enter data 3"))
largest=max(data1,data2,data3)
print(largest)