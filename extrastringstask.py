#create two variables,firstname and lastname and contecanate
firstname="mark"
secname="david"
fullname=firstname+" " +secname
print(fullname)

#given the string word =python,print first and last characters using indexing
word="python"
print(word[0])
print(word[5])

#given the string phase="learning python is fun"use slicing to extract and print"python
phrase="learning python is fun"
print(phrase[9:14])


#given the string text="reverse this",print the reversed version
tex="reverse this"
print(tex[::-1])                                   



#given the string greeting="hello world"replace "world"with python
greeting="hello world"
print(greeting.replace("world","python"))

#take the string msg="python programming"and print it in all uppercase and lower
msg="python programming"
print(msg.lower())
print(msg.upper())

#take the string quotw"the best way to predict the future is to create it"does substring "future"exist?
quote="the best way to predict the future is to create it"
print(quote.count("future"))
print("future" in quote)

#given the string description='data science"print length
des="data science"
print(len(des))



#strinname="   john Doe" remove the leading and trailing spaces
name="    john doe" 
print(name.strip())                               