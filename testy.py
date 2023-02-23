import random
import sys


class Player:
    def __init__(self, race, strength, dexterity, wisdom, charisma):
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.charisma = charisma

    def character_name(self):
        name = input("What would you like your character to be called? ")
        print(f"Is this how you want to call your character? {name}")
        approve = input("To name your character again press 'n'."
                        "\nIf you want to keep the name press any other button on the keyboad.\n ")
        if approve.upper() == "N":  # loop back to the start
            player.character_name()
        else:
            print("The name you've chosen and the qualities your character embodies.")
            self.name = name

    def __str__(self):
        return f"Name: {self.name} | Race: {self.race} | Strength: {self.strength} " \
               f"| Dexterity: {self.dexterity} | Wisdom: {self.wisdom} | Charisma: {self.charisma}"


race_bonuses = {
    "Human": [0, 0, 0, 0],
    "Elf": [0, 2, 0, 2],
    "Dwarf": [-2, 0, 0, 2],
    "Halfling": [0, -2, 0, 0]}

# Ask the player for a number and determine the race based on the number's value
number1 = int(input("Enter a number between 1 and 100: "))
try:
    number1 = int(number1)
except ValueError:
    print("Podany numer nie jest liczbą.")
    sys.exit()


a = range(1, 91)
b = range(90, 95)
c = range(94, 100)
d = range(99, 101)

number2 = int(input("Give a number in a range form 1 to 20: "))
try:
    number2 = int(number2)
except ValueError:
    print("Podany numer nie jest liczbą")
    sys.exit()

if number1 in a:
    race = "Elf"
    zo = [1]
    zp = [2]
    zq = (range(2, 10))
    zr = (range(9, 18))
    zs = (range(17, 21))
    if number2 in zo:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(12, 18) + race_bonuses[race][1]
        wisdom = random.randint(10, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 16) + race_bonuses[race][3]
    elif number2 in zp:
        strength = random.randint(10, 16) + race_bonuses[race][0]
        dexterity = random.randint(8, 14) + race_bonuses[race][1]
        wisdom = random.randint(8, 12) + race_bonuses[race][2]
        charisma = random.randint(8, 12) + race_bonuses[race][3]
    elif number2 in zq:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(14, 18) + race_bonuses[race][1]
        wisdom = random.randint(12, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 14) + race_bonuses[race][3]
    elif number2 in zr:
        strength = random.randint(10, 16) + race_bonuses[race][0]
        dexterity = random.randint(10, 16) + race_bonuses[race][1]
        wisdom = random.randint(10, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 16) + race_bonuses[race][3]
    elif number2 in zs:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(8, 14) + race_bonuses[race][1]
        wisdom = random.randint(8, 12) + race_bonuses[race][2]
        charisma = random.randint(4, 8) + race_bonuses[race][3]
    else:
        print("poza zakresem2")
elif number1 in b:
    race = "Dwarf"
    zo = [1]
    zp = []
    zq = (range(1, 6))
    zr = (range(5, 16))
    zs = (range(15, 21))
    if number2 in zo:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(12, 18) + race_bonuses[race][1]
        wisdom = random.randint(10, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 16) + race_bonuses[race][3]
    elif number2 in zp:
        strength = random.randint(10, 16) + race_bonuses[race][0]
        dexterity = random.randint(8, 14) + race_bonuses[race][1]
        wisdom = random.randint(8, 12) + race_bonuses[race][2]
        charisma = random.randint(8, 12) + race_bonuses[race][3]
    elif number2 in zq:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(14, 18) + race_bonuses[race][1]
        wisdom = random.randint(12, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 14) + race_bonuses[race][3]
    elif number2 in zr:
        strength = random.randint(10, 16) + race_bonuses[race][0]
        dexterity = random.randint(10, 16) + race_bonuses[race][1]
        wisdom = random.randint(10, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 16) + race_bonuses[race][3]
    elif number2 in zs:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(8, 14) + race_bonuses[race][1]
        wisdom = random.randint(8, 12) + race_bonuses[race][2]
        charisma = random.randint(4, 8) + race_bonuses[race][3]
    else:
        print("poza zakresem2")
elif number1 in c:
    race = "Halfling"
    zo = [1]
    zp = []
    zq = (range(1, 13))
    zr = (range(12, 21))
    zs = []
    if number2 in zo:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(12, 18) + race_bonuses[race][1]
        wisdom = random.randint(10, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 16) + race_bonuses[race][3]
    elif number2 in zp:
        strength = random.randint(10, 16) + race_bonuses[race][0]
        dexterity = random.randint(8, 14) + race_bonuses[race][1]
        wisdom = random.randint(8, 12) + race_bonuses[race][2]
        charisma = random.randint(8, 12) + race_bonuses[race][3]
    elif number2 in zq:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(14, 18) + race_bonuses[race][1]
        wisdom = random.randint(12, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 14) + race_bonuses[race][3]
    elif number2 in zr:
        strength = random.randint(10, 16) + race_bonuses[race][0]
        dexterity = random.randint(10, 16) + race_bonuses[race][1]
        wisdom = random.randint(10, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 16) + race_bonuses[race][3]
    elif number2 in zs:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(8, 14) + race_bonuses[race][1]
        wisdom = random.randint(8, 12) + race_bonuses[race][2]
        charisma = random.randint(4, 8) + race_bonuses[race][3]
    else:
        print("poza zakresem2")
elif number1 in d:
    race = "Human"
    zo = []
    zp = (range(0, 6))
    zq = (range(5, 11))
    zr = (range(10, 20))
    zs = [20]
    if number2 in zo:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(12, 18) + race_bonuses[race][1]
        wisdom = random.randint(10, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 16) + race_bonuses[race][3]
    elif number2 in zp:
        strength = random.randint(10, 16) + race_bonuses[race][0]
        dexterity = random.randint(8, 14) + race_bonuses[race][1]
        wisdom = random.randint(8, 12) + race_bonuses[race][2]
        charisma = random.randint(8, 12) + race_bonuses[race][3]
    elif number2 in zq:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(14, 18) + race_bonuses[race][1]
        wisdom = random.randint(12, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 14) + race_bonuses[race][3]
    elif number2 in zr:
        strength = random.randint(10, 16) + race_bonuses[race][0]
        dexterity = random.randint(10, 16) + race_bonuses[race][1]
        wisdom = random.randint(10, 16) + race_bonuses[race][2]
        charisma = random.randint(10, 16) + race_bonuses[race][3]
    elif number2 in zs:
        strength = random.randint(8, 12) + race_bonuses[race][0]
        dexterity = random.randint(8, 14) + race_bonuses[race][1]
        wisdom = random.randint(8, 12) + race_bonuses[race][2]
        charisma = random.randint(4, 8) + race_bonuses[race][3]
    else:
        print("poza zakresem2")
else:
    print("poza zakresem1")

    # Applying the attribute bonuses based on the character's race
    # gives 'Name 'wisdom' can be undefined' back so i changed it
    '''
        strength += race_bonuses[race][0]
        dexterity += race_bonuses[race][1]
        wisdom += race_bonuses[race][2]
        charisma += race_bonuses[race][3]'''

player = Player(race, strength, dexterity, wisdom, charisma)
player.character_name()

print(player)
'''print("Are you happy with the outcome?")
approve = input("To generate your character again press 'n'."
                "\nIf you want to keep the character as it is press any other button on the keyboad.\n ")
if approve.upper() == "N":  # loop back to the start
    player.character_name()
    # figure out how to repeat the number collecting code
else:
    sys.exit()'''
