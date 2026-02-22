
year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")
    
    if year % 4 != 0:
        print("Reason: Not divisible by 4.")
    else:
        print("Reason: Divisible by 100 but not by 400.")