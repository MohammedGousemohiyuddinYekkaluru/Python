## Lets learn it with an example

# correct email = OnMyOwn@gmail.com
# correct password = 9876

email = input("Email : ")
if '@' in email :
    password = input("password : ")

    if email == "OnMyOwn@gmail.com" and password == "9876" :
        print("Successfully loggedin")
    elif email == "OnMyOwn@gmail.com" and password != "9876" :
        print("Incorrect password")
        password = input("Try again!")
        if password == "9876" :
            print("Correct password")
        else:
            print("still incorrect password")
    else:
        print("Credentials are wrong")
else:
    print("Invalid email syntax")