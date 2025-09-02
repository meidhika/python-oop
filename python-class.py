class Hero: #template
    # Class Variabel
    jumlah = 0

    def __init__(self, inputName, inputPower, inputArmor, inputHealth):
        # Instance Variable
        self.name = inputName
        self.power = inputPower
        self.armor = inputArmor
        self.health = inputHealth
        Hero.jumlah += 1
        print("membuat hero dengan nama " + inputName)

hero1 = Hero("sniper", 100,95,1000)
print(Hero.jumlah)
hero2 = Hero("axe", 100,100,1000)
print(Hero.jumlah)
hero3 = Hero("launcher", 100,80,1000)
print(Hero.jumlah)