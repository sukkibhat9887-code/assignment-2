#  Factorial
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

#  Prime Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#  Fibonacci (nth number)
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

#  Sum of Digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

#  Reverse Number
def reverse_number(n):
    return int(str(n)[::-1])

#  Armstrong Number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

#  GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#  LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

#  Perfect Number
def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

#  Menu
def math_menu():
    while True:
        print("\n=== MATH MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 10:
            print("Exiting...")
            break

        elif choice == 1:
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif choice == 2:
            n = int(input("Enter number: "))
            print("Prime:" , is_prime(n))

        elif choice == 3:
            n = int(input("Enter position: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == 4:
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == 5:
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == 6:
            n = int(input("Enter number: "))
            print("Armstrong number:", is_armstrong(n))

        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == 9:
            n = int(input("Enter number: "))
            print("Perfect number:", is_perfect_number(n))

        else:
            print("Invalid choice!")

# Run menu
math_menu()