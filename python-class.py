class Hero:
    def __init__(self, inputName, inputPower, inputArmor, inputHealth):
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor
        self.health = inputHealth

hero1 = Hero("sniper", 100,95,1000)
hero2 = Hero("axe", 100,100,1000)
hero3 = Hero("launcher", 100,80,1000)
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)