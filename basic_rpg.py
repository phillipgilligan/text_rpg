import os
import random
import player
import enemies
import shopinventory

#!#################################################################################################
#!                               Main Start System                                                #
#!#################################################################################################
def start():
    global PlayerIG
    os.system('cls')
    print("Hello what is your name?\n")
    option = input("-->")
    PlayerIG = player.Player(option)
    start1()

def start1():
    os.system('cls')
    print("1. Fight")
    print("2. Store")
    print("3. Inventory")
    print("4. Profile")
    print("5. Exit")
    option = input("--->")
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        inventory()
    elif option == "4":
        profile()
    elif option == "5":
        exit()
    else:
        start1()

#!#################################################################################################
#!                               Profile System                                                   #
#!#################################################################################################    

def profile():
    os.system('cls')
    print(f"Hello, how are you {PlayerIG.name}?")
    print("-"*35)
    print(f"Health: {PlayerIG.health}/{PlayerIG.maxhealth}")
    print(f"Weapon: {PlayerIG.curweap}")
    print(f"Attack: {PlayerIG.attack}")
    print(f"Armor: {PlayerIG.curarmor}")
    print(f"Defense: {PlayerIG.defense}")
    print(f"Gold: {PlayerIG.gold}")
    print(f"Potions: {PlayerIG.pots}")
    print("-"*35)
    print("b. Exit")
    option = input("->")
    if option == "b":
        start1()
    else:
        profile()
    

#!#################################################################################################
#!                               Fighting System                                                  #
#!#################################################################################################        
def prefight():
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = enemies.GoblinIG
    else:
        enemy = enemies.ZombieIG
    fight()

def fight():
    os.system('cls')
    print(f"{PlayerIG.name} vs {enemy.name}")
    print(f"{PlayerIG.name}'s health: {PlayerIG.health}/{PlayerIG.maxhealth} || {enemy.name}'s health: {enemy.health}/{enemy.maxhealth}")
    print(f"Potions: {PlayerIG.pots}")
    print("1. Attack")
    print("2. Drink Potion")
    print ("3. Flee")
    option = input("-> ")
    if option == "1":
        attack()
    elif option == "2":
        drinkpot()
    elif option == "3":
        flee()
    else:
        fight()

def attack():
    os.system('cls')
    pAttack = random.randint(int(PlayerIG.attack / 2), PlayerIG.attack)
    eAttack = random.randint(int(enemy.attack / 2), enemy.attack)
    
    if pAttack == PlayerIG.attack / 2:
        print("You miss!")
    else:
        enemy.health -= pAttack
        print(f"You deal {pAttack} damage!")
    input('')
    os.system('cls')
    
    if enemy.health <= 0:
        win()
    
    if eAttack == enemy.attack / 2:
        print(f"{enemy.name} missed!")
    else:
        if eAttack <= PlayerIG.defense:
            print(f"{enemy.name} did 0 damage!")
        else:
            hit = PlayerIG.defense - eAttack
            print (hit)
            PlayerIG.health -= hit
            print(f"{enemy.name} did {eAttack} damages!")
    input('')
    os.system('cls')
    
    if PlayerIG.health <= 0:
        lose()
    else:
        fight()

def drinkpot():
    os.system('cls')
    if PlayerIG.pots == 0:
        print("You don't have any potions!")
    else:
        PlayerIG.health += 50
        PlayerIG.pots -= 1
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
            print("You are now at max health!")
        else:
            print ("You drank a potion!")
    input('')
    fight()

def flee():
    os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 3:
        print("You have fleed!")
        input("")
        start1()
    else:
        print("You have failed to flee!")
        input("")
        os.system('cls')
        eAttack = random.randint(int(enemy.attack / 2), enemy.attack)
        if eAttack == enemy.attack / 2:
            print(f"{enemy.name} missed!")
        else:
            PlayerIG.health -= eAttack
            print(f"{enemy.name} did {eAttack} damages!")
        if PlayerIG.health <=0:
            lose()
        else:
            fight()

def win():
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldgain
    print(f"You have defeated the {enemy.name}!")
    print(f"You have gained {enemy.goldgain} gold!")
    input("")
    start1()

def lose():
    enemy.health = enemy.maxhealth
    print ("You have Died!")
    input("")   
    start()

#!#################################################################################################
#!                               Store System                                                     #
#!#################################################################################################           
def store():
    os.system('cls')
    print("Welcome to the shop! \nWhat would you like?")
    print("1. Swords")
    print("2. Armor")
    print("3. Items")
    print("b. Back")
    option = input("->")
    if option == "1":
        buysword()
    elif option == "2":
        buyarmor()
    elif option == "3":
        buyitems()
    elif option == "b":
        start1()
    else:
        store()

def buysword():   
    input("")
    os.system('cls')
    for item in shopinventory.sword:
        print (f"{item}, {shopinventory.sword[item]}G")
    print("b. Leave")
    option = input("->")
    if option == "b":
        start1()
    if option in shopinventory.sword:
        if PlayerIG.gold >= shopinventory.sword[option]:
            os.system('cls')
            PlayerIG.gold -= shopinventory.sword[option]
            PlayerIG.weap.append(option)
            print(f"Purchased {option}!")
            store()
        else:
            os.system('cls')
            print ("You don't have enough gold!")
        input("")
        store()
    else:
        os.system('cls')
        print("This item does not exist!")
        input("")
        store()

def buyarmor():   
    input("")
    os.system('cls')
    for item in shopinventory.armor:
        print (f"{item}, {shopinventory.armor[item]}G")
    print("b. Leave")
    print ("")
    option = input("->")
    if option == "b":
        start1()
    if option in shopinventory.armor:
        if PlayerIG.gold >= shopinventory.armor[option]:
            os.system('cls')
            PlayerIG.gold -= shopinventory.armor[option]
            PlayerIG.armor.append(option)
            print(f"Purchased {option}!")
            input("")
            store()
        else:
            os.system('cls')
            print ("You don't have enough gold!")
        input("")
        store()
    else:
        os.system('cls')
        print("This item does not exist!")
        input("")
        store()

def buyitems():   
    input("")
    os.system('cls')
    for item in shopinventory.items:
        print (f"{item}, {shopinventory.items[item]}G")
    print("b. Leave")
    print ("")
    option = input("->")
    if option == "b":
        start1()
    if option in shopinventory.items:
        if PlayerIG.gold >= shopinventory.items[option]:
            os.system('cls')
            PlayerIG.gold -= shopinventory.items[option]
            PlayerIG.pots += 1
            print(f"Purchased {option}!")
            input("")
            store()
        else:
            os.system('cls')
            print ("You don't have enough gold!")
        input("")
        store()
    else:
        os.system('cls')
        print("This item does not exist!")
        input("")
        store()

#!#################################################################################################
#!                               Inventory System                                                 #
#!#################################################################################################    
def inventory():
    os.system('cls')
    print(f"Weapons: {PlayerIG.curweap}")
    print(f"Armor: {PlayerIG.curarmor}")
    print("What do you want to do?")
    print("1. Equip Weapon")
    print("2. Equip Armor")
    print ("b. Go back")
    option = input(">>>")
    if option == "1":
        equipweap()
    if option == "2":
        equiparmor()
    elif option == "b":
        start1()
    else:
        inventory()

def equipweap():
    os.system('cls')
    print("What do you want to equip?")
    for weapon in PlayerIG.weap:
        print (weapon)
    print("b to go back")
    option = input(">>> ")
    if option == PlayerIG.curweap:
        print ("You alread have that weapon equipped!")
        input("")
        equipweap()
    elif option == "b":
        inventory()
    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print (f"You have equipped {option}!")
        input("")
        equipweap()
    else:
        print (f"You don't have {option} in your inventory!")
        equipweap()
        
def equiparmor():
    os.system('cls')
    print("What do you want to equip?")
    for armor in PlayerIG.armor:
        print (armor)
    print("b to go back")
    option = input(">>> ")
    if option == PlayerIG.curarmor:
        print ("You alread have that armor equipped!")
        input("")
        equiparmor()
    elif option == "b":
        inventory()
    elif option in PlayerIG.armor:
        PlayerIG.curarmor = option
        print (f"You have equipped {option}!")
        input("")
        equiparmor()
    else:
        print (f"You don't have {option} in your inventory!")
        equiparmor()

#!#################################################################################################
#!                               Main Function                                                    #
#!#################################################################################################    
def main():
    os.system('cls')
    print ("Welcome to my game!\n")
    print ("1. Start")
    print ("2. Exit")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        exit()
    else:
        print("Invalid selection! Please try again")
        main()
main()