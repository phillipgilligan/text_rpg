import sys
import os
import random
import swords
import enemies

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 0
        self.pots = 0
        self.weap = []
        self.curweap = []
        
    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 5
            
        if self.curweap == "Great Sword":
            attack += 15
            
        if self.curweap == "Lightning Sword":
            attack += 25
                
        if self.curweap == "Ultima Weapon":
            attack += 50
            
        return attack

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

def start():
    global PlayerIG
    os.system('cls')
    print("Hello what is your name?\n")
    option = input("-->")
    PlayerIG = Player(option)
    start1()

def start1():
    os.system('cls')
    print(f"Hello, how are you {PlayerIG.name}?")
    print(f"Attack: {PlayerIG.attack}")
    print(f"Gold: {PlayerIG.gold}")
    print(f"Weapons: {PlayerIG.curweap}")
    print(f"Potions: {PlayerIG.pots}")
    print(f"Health: {PlayerIG.health}/{PlayerIG.maxhealth}")
    print("1. Fight")
    print("2. Store")
    print("3. Inventory")
    print("4. Exit")
    option = input("--->")
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        inventory()
    elif option == "4":
        exit()
    else:
        start1()

def inventory():
    os.system('cls')
    print("What do you want to do?")
    print("1. Equip Weapon")
    print ("b. Go back")
    option = input(">>>")
    if option == "1":
        equip()
    elif option == "b":
        start1()
    else:
        inventory()

def equip():
    os.system('cls')
    print("What do you want to equip?")
    for weapon in PlayerIG.weap:
        print (weapon)
    print("b to go back")
    option = input(">>> ")
    if option == PlayerIG.curweap:
        print ("You alread have that weapon equipped!")
        input("")
        equip()
    elif option == "b":
        inventory()
    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print (f"You have equipped {option}!")
        input("")
        equip()
    else:
        print (f"You don't have {option} in your inventory!")
        equip()

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
    # #pAttack = random.randint(1, 10)
    # #eAttack = random.randint(1, 10)
    
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
        PlayerIG.health -= eAttack
        print(f"{enemy.name} did {eAttack} damages!")
    input('')
    os.system('cls')
    
    if PlayerIG.health <= 0:
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

def store():
    os.system('cls')
    print("Welcome to the shop! \nWhat would you like to buy?")
    input("")
    os.system('cls')
    for item in swords.weapons:
        print (f"{item}, {swords.weapons[item]}G")
    print("b. Leave")
    print ("")
    option = input("->")
    if option == "b":
        start1()
    if option in swords.weapons:
        if PlayerIG.gold >= swords.weapons[option]:
            os.system('cls')
            PlayerIG.gold -= swords.weapons[option]
            PlayerIG.weap.append(option)
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
main()