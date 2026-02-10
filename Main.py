#example = ['a', 'b', 'c', 'd', 'e']
#print(random.choice(example)) - credits to stackoverflow.com
import random
#p stands for preset
def pbank_process():
    pword = random.choice(presetwb)
def menu():
    print("To begin the program input a number in order to access the Vocabulary Quiz Generator!\n Type 1 in order to access a preset word bank.\n", "Type 2 in order to enter words in.\n", "Type 3 in order to access the custom word bank.\n", "Type 4 if you need help understanding how the quiz works.\n", "Type 5 to exit the program")
    print("-")*30

def exit():
    

    
custombank = []
presetwb = ["House","Tree","Shop","Planet","River","Time", "Year", "Person", "Highway", "Day", "Man"]
def fullReset():
    while len(custombank) > 0:
        custombank.pop

choice = input("Type Here: ")
if choice == "1":
    pbank_process
elif choice == "3":

elif choice == "4":
    print("The code functions by giving the definition of the word and then prompting the user to input what word they believe it is.\nTyping 'exit' brings user to back to the main menu")
    