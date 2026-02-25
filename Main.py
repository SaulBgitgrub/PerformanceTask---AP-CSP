# This segment gives an error message when a non-integar value is input after an operation has been input.
def get_bool(message, error = "---That wasn't an integer---"):
    try:
        return int(input(message))
    except ValueError:
        print(error)
        get_bool(message, error)
#This part is simply for stating what operation the user selected in order during the what "number would you like to ???"
def stringify_operation(operation):
    if operation == "/":
        return "divide"
    elif operation == "*":
        return "multiply"
    elif operation == "+":
        return "add"
    elif operation == "-":
        return "subtract"
    else:
        return ""
#This is the function that tells the user what numbers to type
def help():
    print("To begin the program input a number in order to access the Math Practice Tool!")
    print("+ Type 1 in order to access the calculator.")
    print("+ Type 2 if you need help understanding how the program works.")
    print("+ Type 3 to exit the program")
    print("-----")
#The main screen that the user will look at
def main():
    help()
    selection()
#Where the user types in their choice of number
def selection():
    x = input("Type Here: ")
    if x == "1":
        process()
    elif x == "2":
        help_2()
    elif x == "3":
        print("Thank you for your time!")
        return
    else:
        print("Invalid expression")

    main()
#This list has the valid symbols that can be input by the user. They aren't used in the help_2 function since they still have the ' symbol attached to each one ex: '+'
valid_symbols = ["-", "+", "*", "/"]
#This function is for the second option when the user types 2
def help_2():
    print("-----")
    print("In order to use the calculator, you just have to type in one of the following symbols ( -, +, *, or / ).")
    print("The user is returned to the main menu after a calculation or when they add an invalid expression.")
    print("-----")
#The calculator itself alongside its many options to handle errors is present in the process function.
def process():
    decision = input("Which form of equation would you like to use: ")
    if decision not in valid_symbols:
        print("---Invalid symbol---")
        return
    operation = stringify_operation(decision)
    x = get_bool(f"What is your first number you would like to {operation}: ")
    y = get_bool(f"What is your second number you would like to {operation}: ")
    if decision == "/":
        while y != 0:
            try:
                print(x / y)
                break
            except TypeError:
                print("---Calculation stopped due to previously input non-integar---")
                break
        else:
            return print("No dividing by zero!")
    elif decision == "*":
        try:
            print(x * y)
        except TypeError:
            print("---Calculation stopped due to previously input non-integar---")
    elif decision == "+":
        try:
            print(x + y)
        except TypeError:
            print("---Calculation stopped due to previously input non-integar---")
    elif decision == "-":
        try:
            print(x - y)
        except TypeError:
            print("---Calculation stopped due to previously input non-integar---")

main()