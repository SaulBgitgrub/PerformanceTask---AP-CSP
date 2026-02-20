def get_bool(message, error = "---That wasn't an integer---"):
    try:
        return int(input(message))
    except ValueError:
        print(error)
        get_bool(message, error)

def stringify_operation(operation):
    if operation == "/":
        return "divide"
    elif operation == "&":
        return "multiply"
    elif operation == "+":
        return "add"
    elif operation == "-":
        return "subtract"
    else:
        return ""

def help():
    print("To begin the program input a number in order to access the Math Practice Tool!")
    print("+ Type 1 in order to access the calculator.")
    print("+ Type 2 if you need help understanding how the program works.")
    print("+ Type 3 to exit the program")
    print("-----")

def main():
    help()
    selection()

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

def help_2():
    print("-----")
    print("In order to use the calculator, you just have to type in one of the following symbols ( -, +, *, or / ). ")
    print("The user is returned to the main menu after a calculation or when they add an invalid expression.")
    print("-----")

def process():
    decision = input("Which form of equation would you like to use: ")
    if decision not in ["*", "/", "+", "-"]:
        print("---Invalid symbol---")
        return
    operation = stringify_operation(decision)
    x = get_bool(f"What is your first number you would like to {operation}: ")
    y = get_bool(f"What is your second number you would like to {operation}: ")
    if decision == "/":
        if y == 0:
            print("No dividing by zero!")
            return
        print(x / y)
    elif decision == "*":
        print(x * y)
    elif decision == "+":
        print(x + y)
    elif decision == "-":
        print(x - y)

main()