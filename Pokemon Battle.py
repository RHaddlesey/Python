#Pokeballs~~~~~
pokeballchance = 30
#~~~~~~~~~~~~~~

import random

def attack():
    print ("which move do you want to use, 1, 2, 3 or 4")
    Move1 = int(input())
    
    critical = random.randrange(0,100)
    chance = 10
    if Move1 == 1:
        if critical <= chance:
            print ("You got a critical hit!")
            print ("You used Tackle!")
            print (enemy," lost 15 HP")
        else:
            print ("You used Tackle!")
            print (enemy," lost 10 HP")
        Hp1 = Hp1 - 10
        PP_m1 = PP_m1 - 1
        
    elif Move1 == 2:
        print ("You used Swagger!")
        print ("you gained 10% Critical hit chance!")
        PP_m2 = PP_m2 - 1
        
    elif Move1 == 3:
        print ("You used Screech!")
        print ("Bidoof lost 10% attack Damage!")
        B_attack = B_attack - 10
        PP_m3 = PP_m3 - 1

    elif Move1 == 4:
        if critical <= chance:
            print ("You got a critical hit!")
            print ("You used Pound!")
            print ("Bidoof lost 20 HP")
        else:
            print ("You used Pound!")
            print ("Bidoof lost 15 HP")
        Hp1 = Hp1 - 15
        PP_m4 = PP_m4 - 1


def battlesequence():
    wanttobattle = 'y'
    starter = 'n'
    while wanttobattle == 'y':
        teamcount = 0
        if starter == 'n':
            choice = int(input("What starter pokemon do you choose, 1, 2 or 3? :"))
            if choice == 1:
                print ("You summoned Piplup!")
                HP = 60
                inventory = ["(1) Pokeball","(2) Elixar","(3) Max Potion","(4) Water Shell"]
                team = ["(1)Piplup"]
                starter = 'y'
                
            elif choice == 2:
                print ("You summoned Turtlewig!")
                HP = 65
                inventory = ["(1) Pokeball","(2) Elixar","(3) Max Potion","(4) Crystal Leaf"]
                team = ["(2)Turtlewig"]
                starter = 'y'
                
            elif choice == 3:
                print ("You summoned Chimchar!")
                HP = 55
                inventory = ["(1) Pokeball","(2) Elixar","(3) Max Potion","(4) Fire Stone"]
                team = ["(3)Chimchar"]
                starter = 'y'
        elif starter == 'y':

            money = 0

            pc = []
            pcremaining = 30

            PP_m1 = 15
            PP_m2 = 30
            PP_m3 = 25
            PP_m4 = 10
            encounterchance = random.randint(0,100)
            if encounterchance <= 60:
                enemy = 'Bidoof'
            elif encounterchance >=61:
                enemy = 'Starly'
            name = input("Welcome to pokemon! What is your name? :")
            teamcount = teamcount + 1 
            print ("Your Hp is ", HP)
            print ("You have $",money)
            print ("Oh no ",name,", You are under attack by a wild ",enemy,"!")
            print ("What pokemon do you want to summon? ",team[0])
            pokesummonchoice = input()
            if enemy == 'Bidoof':
                B_attack = 100
                Hp1 = 50
            elif enemy == 'Starly':
                B_attack = 100
                Hp1 = 40
            while Hp1 and HP > 0:
                if pokesummonchoice == 1:
                    print ("You chose ",team[0],"!")
                
                print (enemy," has ", Hp1," HP left!")
                if B_attack == 100:
                    print (enemy," used Tackle! You lost 15 HP!")
                    HP = HP - 15
                elif B_attack == 90:
                    print (enemy," used Tackle! You lost 14 HP!")
                    HP = HP - 14
                elif B_attack == 80:
                    print (enemy," used Tackle! You lost 13 HP!")
                    HP = HP - 13
                elif B_attack == 70:
                    print (enemy," used Tackle! You lost 12 HP!")
                    HP = HP - 12
                elif B_attack == 60:
                    print (enemy," used Tackle! You lost 11 HP!")
                    HP = HP - 11
                elif B_attack == 50:
                    print (enemy," used Tackle! You lost 10 HP!")
                    HP = HP - 10
                elif B_attack == 40:
                    print (enemy," used Tackle! You lost 9 HP!")
                    HP = HP - 9
                elif B_attack == 30:
                    print (enemy," used Tackle! You lost 8 HP!")
                    HP = HP - 8
                elif B_attack == 20:
                    print (enemy," used Tackle! You lost 7 HP!")
                    HP = HP - 7
                else:
                    print (enemy,"'s attack cannot be lowered any further!")
                    print (enemy," used Tackle! You lost 5 HP!")
                    HP = HP - 5
                    
                if Hp1 <= 0:
                    print (enemy," fainted!")
                    Exp = random.randrange(50, 700)
                    print ("You Gained ", Exp,"Exp!")
                    exit()
                elif HP <= 0:
                    print ("You Fainted!")
                    lostmoney = random.randrange(50, 700)
                    if money <= 0:
                        print ("You have no money to lose!")
                    else:
                        print ("You lost ", Money,"Money!")
                        if money <= 0:
                            money = 0
                        else:
                            print ("You now have $",money)
                    true = 1
                    while true == 1:
                        live = input("Would you loke to go to the pokemon centre? y / n ? :").lower()
                        if live == 'y':
                            print ("You arrive at the pokemon centre!")
                            print ("All Your Pokemon Are healed!")
                            if choice == 1:
                                HP = 60
                            elif choice == 2:
                                HP = 65
                            elif choice == 3:
                                HP = 55
                            print (team[0],"was healed!")
                            if enemy == 'Bidoof':
                                Hp1 = 50
                            elif enemy == 'Starly':
                                Hp1 = 40
                            print (team[1],"was healed!")
                            true = 0
                        elif live == 'n':
                            exit()
                        else:
                            print ("please enter a valid answer (y / n)")
                        

                else:
                    print ("Your HP is ", HP)
                    option = input("Do you want to use an item? ").lower()
                    if option == 'yes':
                        print ("which item do you want to use?!")
                        print (inventory)
                        item = input()
                        if item == '1':
                            print ("You used a pokeball!")
                            catchchance = random.randint(0,100)
                            if catchchance <= pokeballchance:
                                print ("You caught a(n) ",enemy,"!")
                                if enemy == 'Bidoof':
                                    Hp1 = 50
                                    team.append("(4) Bidoof")
                                elif enemy == 'Starly':
                                    team.append("(4)Starly")
                                    Hp1 = 40
                                inventory.remove('(1) Pokeball')
                                if teamcount <= 5:
                                    print (enemy," has joined your team!")
                                elif pcremaining != 0:
                                    print ("Your Team is full! ",enemy,"was sent to your PC!")
                                else:
                                    print ("You cannot hold anymore pokemon! ",enemy," was set free!")
                                break
                            else:
                                print ("It Failed!")
                        elif item == '2':
                            print("All of your pokemon's Moves were replenished!")
                            PP_m1 = 15
                            PP_m2 = 30
                            PP_m3 = 25
                            PP_m4 = 10
                            inventory.remove("(2) Elixar")
                        elif item == '3':
                            inventory.remove("(3) Max Potion")
                            print ("which pokemon do you want to heal? ",team,"!")
                            healchoice = input().lower()
                            if healchoice == 1:
                                print (team[0],"was healed!")
                                
                            elif healchoice == 2:
                                print (team[0],"was healed!")
                                
                            elif healchoice == 3:
                                print (team[0],"was healed!")
                            
                            inventory.remove[2]
                            if healchoice == 4:
                                if enemy == 'Bidoof':
                                    Hp1 = 50
                                elif enemy == 'Starly':
                                    Hp1 = 40
                            print (team[1],"was healed!")
                            inventory.remove[2]
                        elif item == '4':
                            print ("Your Pokemon's critical chance was increased by 40!")
                            chance = chance + 40
                            inventory.remove[3]
                            
                        
                        
                    elif option == 'no':
                        print ("Ok!")

                    print ("which move do you want to use, 1, 2, 3 or 4")
                    Move1 = int(input())
                    
                    critical = random.randrange(0,100)
                    chance = 10
                    if Move1 == 1:
                        if critical <= chance:
                            print ("You got a critical hit!")
                            print ("You used Tackle!")
                            print (enemy," lost 15 HP")
                        else:
                            print ("You used Tackle!")
                            print (enemy," lost 10 HP")
                        Hp1 = Hp1 - 10
                        PP_m1 = PP_m1 - 1
                        
                    elif Move1 == 2:
                        print ("You used Swagger!")
                        print ("you gained 10% Critical hit chance!")
                        PP_m2 = PP_m2 - 1
                        
                    elif Move1 == 3:
                        print ("You used Screech!")
                        print ("Bidoof lost 10% attack Damage!")
                        B_attack = B_attack - 10
                        PP_m3 = PP_m3 - 1

                    elif Move1 == 4:
                        if critical <= chance:
                            print ("You got a critical hit!")
                            print ("You used Pound!")
                            print ("Bidoof lost 20 HP")
                        else:
                            print ("You used Pound!")
                            print ("Bidoof lost 15 HP")
                        Hp1 = Hp1 - 15
                        PP_m4 = PP_m4 - 1

battlesequence()   
