#example = ['a', 'b', 'c', 'd', 'e']
#print(random.choice(example)) - credits to stackoverflow.com

def menu():
    print("To begin the program input a number in order to access the Math Practice Tool!\n+ Type 1 in order to access the custom word bank.\n+ Type 2 if you need help understanding how the program works.\n+ Type 3 to exit the program\n-----")
def exit():
    pass
def c4():
    print("-----\nThe code functions by giving the definition of the word and then prompting the user to input what word they believe it is.\nTyping 'exit' brings user to back to the main menu.\n -----")
    return menu()
def divpro(x,y):
    total = x/y
    return total
def process():
    decision = input("Which form of equation would you like to use: ")
    if decision == "/":
        o = int(input("What is your first number you would like to divide: "))
        p = int(input("What is your second number you would like to divide: "))
        divpro(o,p)






menu()
choice = input("Type Here: ")
if choice == "1":
    print(process())
elif choice == "2":
    c4()
    choice = input("Type Here: ")
elif choice == "3":
    print(" ")