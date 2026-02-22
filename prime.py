num = int(input("Enter a number: "))

if num < 0:
    print(num, "Enter another number")
elif num == 0 or num == 1:
    print(num, "is not a prime number.")
elif num == 2:
    print("2 is a prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for n in range(start, end + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end=", ")