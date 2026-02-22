
def add(a, b): #addition
    return a + b

def subtract(a, b): #subtraction
    return a - b

def multiply(a, b): #multiplication
    return a * b

def divide(a, b): #division
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b): #modulus
    return a % b

def power(a, b): #power
    return a ** b

def calculator(): #main calculator
    while True:
        print("=== CALCULATOR MENU ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            print("Exiting calculator...")
            break

        if choice in [1, 2, 3, 4, 5, 6]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(a, b))
            elif choice == 2:
                print("Result:", subtract(a, b))
            elif choice == 3:
                print("Result:", multiply(a, b))
            elif choice == 4:
                print("Result:", divide(a, b))
            elif choice == 5:
                print("Result:", modulus(a, b))
            elif choice == 6:
                print("Result:", power(a, b))
        else:
            print("Invalid choice! Please select 1-7.")

calculator() #call calculator