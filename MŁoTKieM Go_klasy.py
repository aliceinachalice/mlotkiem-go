import random
import sys


class Player:
    def __init__(self, name, race, strength, dexterity, wisdom, charisma):
        self.name = name
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.charisma = charisma

    def __str__(self):
        return f" Name {self.name} | Race {self.race} | Str {self.strength} " \
               f"| Dex {self.dexterity} | Wis {self.wisdom} | Cha {self.charisma}"

    def character_name(self, name):
        self.name = input("What would you like your character to be called? ")
        print(f"Is this how you want to call your character? {name}")
        approve = input("To name your character again press 'n'."
                        "\nIf you want to keep the name enter any other character.\n ")
        if approve.upper() == "N":  # loop back to the start
            player.character_name(name)

    def set_strength_elf(self, number2, zo, zp, zq, zr, zs):
        if number2 in zo:
            self.strength = random.randint(1, 5)
        elif number2 in zp:
            self.strength = random.randint(6, 10)
        elif number2 in zq:
            self.strength = random.randint(11, 15)
        elif number2 in zr:
            self.strength = random.randint(16, 20)
        elif number2 in zs:
            self.strength = random.randint(21, 25)
        else:
            print("Podany numer nie mieści się w zakresie 1-20.")
            sys.exit()


    def set_dexterity_elf(self, number2, zo, zp, zq, zr, zs):
        if number2 in zo:
            self.dexterity = random.randint(21, 25)
        elif number2 in zp:
            self.dexterity = random.randint(16, 20)
        elif number2 in zq:
            self.dexterity = random.randint(11, 15)
        elif number2 in zr:
            self.dexterity = random.randint(6, 10)
        elif number2 in zs:
            self.dexterity = random.randint(1, 5)
        else:
            print("poza zakresem 2")

    def set_wisdom_elf(self, number2, zo, zp, zq, zr, zs):
        if number2 in zo:
            self.wisdom = random.randint(1, 5)
        elif number2 in zp:
            self.wisdom = random.randint(6, 10)
        elif number2 in zq:
            self.wisdom = random.randint(11, 15)
        elif number2 in zr:
            self.wisdom = random.randint(16, 20)
        elif number2 in zs:
            self.wisdom = random.randint(21, 25)
        else:
            print("poza zakresem 2")

    def set_charisma_elf(self, number2, zo, zp, zq, zr, zs):
        if number2 in zo:
            self.charisma = random.randint(21, 25)
        elif number2 in zp:
            self.charisma = random.randint(16, 20)
        elif number2 in zq:
            self.charisma = random.randint(11, 15)
        elif number2 in zr:
            self.charisma = random.randint(6, 10)
        elif number2 in zs:
            self.charisma = random.randint(1, 5)
        else:
            print("poza zakresem 2")


a = range(1, 91)
b = range(90, 95)
c = range(94, 100)
d = range(99, 101)

zo = [1]
zp = [2]
zq = (range(2, 10))
zr = (range(9, 18))
zs = (range(17, 21))

player = Player(name = None, race = None, strength=0, dexterity=0, wisdom=0, charisma=0)

while True:
    player.character_name(name = None)
    number1 = int(input("Podaj liczbę z zakresu 1-100: "))
    number2 = int(input("Podaj liczbę z zakresu 1-20: "))

    if number1 in a:
        player.race = "Elf"
        player.set_strength_elf(number2, zo, zp, zq, zr, zs)
        player.set_dexterity_elf(number2, zo, zp, zq, zr, zs)
        player.set_wisdom_elf(number2, zo, zp, zq, zr, zs)
        player.set_charisma_elf(number2, zo, zp, zq, zr, zs)
    elif number1 in b:
        player.race = "Dwarf"
        # jak ustanowie wartości, to przy tworzeniu będą dostawali
        # swoje wartości atrybutów, i nie będą brać z wcześniej utworzonego
    elif number1 in c:
        player.race = "Halfling"
    elif number1 in d:
        player.race = "Human"
    else:
        print("Podany numer nie mieści się w zakresie 1-100")
        break

    # player.set_strength(number1, a, b, c, d)
    print(player)

    play_again = input("Are you happy with how the character you've got? (y/n): ")
    if play_again.lower() == "n":
        print("Let's take another try then!")
    elif play_again.lower() == "y":
        print("We're done here then!")
        break
    else:
        print("Invalid answer, run the code again.")
        break
