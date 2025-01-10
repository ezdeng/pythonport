#Eva D.
#P1. 11/19/24

#Simple Calculator

#init
#functions
def add(num1, num2):
    print(num1 + num2)

def sub(num1, num2):
    print(num1 - num2)

def multi(num1, num2):
    print(num1 * num2)

def divi(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1 / num2)

#main
print("Welcome to Simple Calculator!")

def simplecal():
    while True:
        print("Select an operation")
        print("\n1. Addition \n2. Subtraction \n3. Multiplication  \n4. Division \n5. Quit")
        try:
            option = int(input("Select option(1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if option == 1:
            int1 = int(input("Enter first number: "))
            int2 = int(input("Enter second number: "))
            add(int1, int2)

        elif option == 2:
            int1 = int(input("Enter first number: "))
            int2 = int(input("Enter second number: "))
            sub(int1, int2)

        elif option == 3:
            int1 = int(input("Enter first number: "))
            int2 = int(input("Enter second number: "))
            multi(int1, int2)

        elif option == 4:
            int1 = int(input("Enter first number: "))
            int2 = int(input("Enter second number: "))
            divi(int1, int2)

        elif option == 5:
            print("Thank you for using Simple Calculator!")
            break

        else:
            print("Invalid option. Please select a number between 1 and 5.")
            continue

        # Prompt user to decide whether to continue or quit
        while True:
            choice = input("Would you like to return to the menu? (yes/no): ")
            if choice == "yes":
                break  # Exit this loop to return to the menu
            elif choice == "no":
                print("Thank you for using Simple Calculator, Goodbye!")
                return  # Exit the simplecal function entirely
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

simplecal()
