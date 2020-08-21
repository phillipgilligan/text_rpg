import sys
import os
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.pots = 0

class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10     
GoblinIG = Goblin("Goblin")

class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 15     
ZombieIG = Zombie("Zombie")
        
def main():
    os.system('cls')
    print ("Welcome to my game!\n")
    print ("1. Start")
    print ("2. Load")
    print ("3. Exit")
    option = input("-> ")
    if option == "1":
        start()
        pass
    elif option == "2":
        #load()
        pass
    elif option == "3":
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
    print(f"Potions: {PlayerIG.pots}")
    print(f"Health: {PlayerIG.health}/{PlayerIG.maxhealth}")
    print("1. Fight")
    print("2. Store")
    print("3. Save")
    print("4. Exit")
    option = input("--->")
    if option == "1":
        prefight()
        pass
    elif option == "2":
        store()
        pass
    elif option == "3":
        #save()
        pass
    elif option == "4":
        exit()
    else:
        start1()

def prefight():
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = GoblinIG
    else:
        enemy = ZombieIG
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
    pAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    eAttack = random.randint(enemy.attack / 2, enemy.attack)
    
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
    pass

def lose():
    pass

def drinkpot():
    os.system('cls')
    if PlayerIG.pots == 0:
        print("You don't have any potions!")
        input('')
        fight()
    else:
        PlayerIG.health +- 50
        #! <- This is where I left off ->
        #if
        print ("You drank a potion")

def flee():
    pass

def store():
    pass
    
main()