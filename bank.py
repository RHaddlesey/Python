import time
from random import randint
bank=(randint(50,250))

print("Do you want to know your balance?")
balance = input()
if balance == "yes":
    print("your balance is",bank)
    time.sleep(1)

else:
    break

print("How much do you want to withdraw, £10 or £20?")
withdraw = int(input())
try:
    int=(withdraw)
except ValueError:
    print ("oop")

if withdraw >250:
    print("The withdrawl amount must not be above 250")
    
else:
    final = (bank - withdraw)
    print("Your final balance after withdrawl is",final)
