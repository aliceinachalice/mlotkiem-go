#import random
"""
skomplikować tak żeby mozna wybrać z abc i d
def zakres_1
print(random.choice(range(1,100)))
number2=(random(range(1,20))
zakategoryzuj number2 do ZO...ZS
podaj kategorie, np. A-ZQ
zrobić loop"""
'''
for number2 in range(1,20):
    print("ZO")
    for number2 in ZP:
        print("ZP")
        for number2 in ZQ:
            print("ZQ")
            for number2 in ZR:
                print("ZR")
                for number2 in ZS:
                    print("ZS")'''
"""
number1=(random.randint(1,100))
# number1=(random.choice(A))
# number1=100"""
def repeat():
    number1=int(input("Enter a number in a range form 0 to 100: "))
    # print(type(number1))
   # print("number1 =",number1)

    A=range(1,91)
    B=range(90,95)
    C=range(94,100)
    D=range(99,101)

    number2=int(input("Enter a number in a range form 0 to 20: "))


    if number1 in A:
       # print("A")
        # jesli number1 nalezy do a to numer2 ma:
        ZO = [1]
        ZP = [2]
        ZQ = (range(2, 10))
        ZR = (range(9, 18))
        ZS = (range(17, 21))

       # number2 = (random.randint(1, 20))
       # print("number2 =", number2)

        if number2 in ZO:
            print("A-ZO")
        elif number2 in ZP:
            print("A-ZP")
        elif number2 in ZQ:
            print("A-ZQ")
        elif number2 in ZR:
            print("A-ZR")
        elif number2 in ZS:
            print("A-ZS")
        else:
            print("Second number out of range.")
    elif number1 in B:
       # print("n1 należy do B")
        ZO = [1]
        ZP = []
        ZQ = (range(1, 6))
        ZR = (range(5, 16))
        ZS = (range(15, 21))

       # number2 = (random.randint(1, 20))
       # print("number2 =", number2)

        if number2 in ZO:
            print("B-ZO")
        elif number2 in ZP:
            print("B-ZP")
        elif number2 in ZQ:
            print("B-ZQ")
        elif number2 in ZR:
            print("B-ZR")
        elif number2 in ZS:
            print("B-ZS")
        else:
            print("Second number out of range.")
    elif number1 in C:
       # print("n1 należy do C")
        ZO = [1]
        ZP = []
        ZQ = (range(1, 13))
        ZR = (range(12, 21))
        ZS = []

       # number2 = (random.randint(1, 20))
       # print("number2 =", number2)

        if number2 in ZO:
            print("C-ZO")
        elif number2 in ZP:
            print("C-ZP")
        elif number2 in ZQ:
            print("C-ZQ")
        elif number2 in ZR:
            print("C-ZR")
        elif number2 in ZS:
            print("C-ZS")
        else:
            print("Second number out of range.")
    elif number1 in D:
       # print("n1 należy do D")
        ZO = []
        ZP = (range(0,6))
        ZQ = (range(5, 11))
        ZR = (range(10, 20))
        ZS = [20]

       # number2 = (random.randint(1, 20))
        # number2=1
       # print("number2 =", number2)

        if number2 in ZO:
            print("D-ZO")
        elif number2 in ZP:
            print("D-ZP")
        elif number2 in ZQ:
            print("D-ZQ")
        elif number2 in ZR:
            print("D-ZR")
        elif number2 in ZS:
            print("D-ZS")
        else:
            print("Second number out of range.")
    else:
        print("First number out of range.")
    check = input("To restart enter Y, to end enter any other character.")
    if check.upper() == "Y":  # loop back to the start
        repeat()
    else:
        print("No i fajnie...")
repeat()



