#Password Checker

print("Welcome to PGO Security Systems")
print("*******************************")

attempts = 0
while attempts != 3:
    password = input("Enter your password: ")
    attempts = attempts + 1
    if password == "abcd1234":
        print("Access Granted")
        attempts = 3 #What happens if this statement is left out?
    else:
        print("password incorrect")
        
if password != "abcd1234":
    print("You are locked out")
        
input("Press ENTER to exit the program")


