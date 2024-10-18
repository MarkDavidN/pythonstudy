#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”
#Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
#Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.


name='   JOHn .'
name=name.lower()
print(name)
name=name.replace('.', '')
print(name)
name=name.strip()
print(name)

##Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence1="the dog breed is german shepherd"
print(sentence1[8:23])
sentence2="defeats for the clinton forces,this was her moment of truimph"
print(sentence2[17:30])

##Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
sentence1="the lazy dog;ran so fast;it hit the wall"
print(sentence1.split( ))
print(len(sentence1))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
firstname="   joh.n"
lastname="  do,e"
firstname1=firstname.strip()
print(firstname1)
lastname1=lastname.strip()
print(lastname1)
firstname2=firstname1.replace(".","")
print(firstname2)
lastname2=lastname1.replace(",","")
print(lastname2)
fullname=firstname2+" "+lastname2
print(fullname)

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r='["E","W","C"]'
r=r.replace(" ' ", " ")
print(r)
r=r.replace(","," ")
print(r)
r=r.replace(' [] ',' ')
print(r)