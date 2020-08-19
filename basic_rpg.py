import sys
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        
        
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
    os.system('cls')
    print("Hello what is your name?\n")
    option = input("-->")
    PlayerIG = Player(option)
    start1(PlayerIG)
    
def start1(PlayerIG):
    os.system('cls')
    print(f"Hello, how are you {PlayerIG.name}?")
    print(f"Attack: {PlayerIG.attack}")
    print(f"Health: {PlayerIG.health}/{PlayerIG.maxhealth}")
    print("1. Fight")
    print("2. Store")
    print("3. Save")
    print("4. Exit")
    option = input("--->")
    if option == "1":
        fight()
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
        start1(PlayerIG)
        
def fight():
    pass

def store():
    pass
    
main()