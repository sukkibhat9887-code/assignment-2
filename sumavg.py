n = int(input("How many numbers? "))

tot = 0
max = float('-inf') #Negative Infinity
min = float('inf') #Positive Infinity

for i in range(1, n + 1):
    n = float(input("Enter number: "))
    tot += n
    
    if n > max:
        max = n
    if n < min:
        min = n

avg = tot / n

print("Sum:", tot)
print("Average:", avg)
print("Maximum:", max)
print("Minimum:", min)