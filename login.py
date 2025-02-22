
def userLogin():
        print("Enter your userName")
        username=input()
        print("Enter Password")
        password=input()
        if username=="Xalco" and password=="ujuzi@2025":
                print("Login Successful")
        else:
                print("Invalid Username or Password, Try Again")
                userLogin()
userLogin()





