#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
password=input("enter password")
correctpassword="admin@123"

count = 0
while count < 5:
    count += 1
    if password == correctpassword:
        print("Correct password")
        break
    if count == 4:
        print("Account blocked")
        break
    print("Incorrect password")
    password = input("enter password")


    