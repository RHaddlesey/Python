#Dice Roll Counter

import random
DiceRoll = random.randint(1, 6)
Counter = 1
print (DiceRoll)
while DiceRoll != 6:
    DiceRoll = random.randint(1, 6)
    Counter = Counter + 1
    print(DiceRoll)
print ("Number of rolls:",Counter)
