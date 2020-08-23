class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.base_defense = 10
        self.gold = 0
        self.pots = 0
        self.weap = []
        self.curweap = []
        self.armor = []
        self.curarmor = []

    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Small Dagger":
            attack += 5

        if self.curweap == "Copper Sword":
            attack += 10

        if self.curweap == "Iron Sword":
            attack += 15

        if self.curweap == "Bronze Sword":
            attack += 20

        if self.curweap == "Steel Sword":
            attack += 25
        
        if self.curweap == "Diamond Sword":
            attack += 30

        return attack
    
    @property
    def defense(self):
        defense = self.base_defense
        if self.curarmor == "Leather Armor":
            defense += 5

        if self.curarmor == "Copper Armor":
            defense += 10

        if self.curarmor == "Iron Armor":
            defense += 15

        if self.curarmor == "Bronze Armor":
            defense += 20

        if self.curarmor == "Steel Armor":
            defense += 25
        
        if self.curarmor == "Diamond Armor":
            defense += 30

        return defense