import sys
#Credits to https://www.janbasktraining.com/ for the information regarding sys.exit()

def menu():
    return print("To begin the program input a number in order to access the Math Practice Tool!\n+ Type 1 in order to access the calculator.\n+ Type 2 if you need help understanding how the program works.\n+ Type 3 to exit the program\n-----")
def sel(x):
    if x == "1":
        process()
    elif x == "2":
        c2()
        realmenu()
    elif x == "3":
        print("Thank you for your time!")
        #sys.exit() simply stops the entire program
        sys.exit()
    else:
        print("Invalid expression")
    return realmenu()
def exit():
    pass
def c2():
    print("-----\nIn order to use the calculator, you just have to type in one of the following symbols ( -, +, *, or / ). \nThe user is returned to the main menu after a calculation or when they add an invalid expression.\n -----")
    realmenu()
def divpro(x,y):
    total = x/y
    return total
def timespro(x,y):
    total = x*y
    return total
def addpro(x,y):
    total = x+y
    return total
def minpro(x,y):
    total = x-y
    return total
def process():
    decision = input("Which form of equation would you like to use: ")
    if decision == "/":
        x = int(input("What is your first number you would like to divide: "))
        y = int(input("What is your second number you would like to divide: "))
        return divpro(x,y)
    elif decision == "*":
        x = int(input("What is your first number you would like to multiply: "))
        y = int(input("What is your second number you would like to multiply: "))
        return timespro(x,y)
    elif decision == "+":
        x = int(input("What is your first number you would like to add: "))
        y = int(input("What is your second number you would like to add: "))
        return addpro(x,y)
    elif decision == "-":
        x = int(input("What is your first number you would like to subtract: "))
        y = int(input("What is your second number you would like to subtract: "))
        return minpro(x,y)
    else:
        print("Invalid symbol")
        realmenu()
def realmenu():
    menu()
    x = input("Type Here: ")
    sel(x)

realmenu()

# choice = input("Type Here: ")
# if choice == "1":
#     print(process())
# elif choice == "2":
#     c2()
#     choice = input("Type Here: ")
# elif choice == "3":
#     print("Thank you for your time!")
# else:
#     print("Invalid expression")
#     menu()