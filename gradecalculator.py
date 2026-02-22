
a = float(input("Enter marks for Subject 1: ")) #input of 5 subjects
b = float(input("Enter marks for Subject 2: "))
c = float(input("Enter marks for Subject 3: "))
d = float(input("Enter marks for Subject 4: "))
e = float(input("Enter marks for Subject 5: "))

# Calculating total and percentage
total = a + b + c + d + e
percentage = (total / 500) * 100

# Determining grade
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Determining result
if a >= 40 and b >= 40 and c >= 40 and d >= 40 and e >= 40:
    result = "Pass"
else:
    result = "Fail"

# Displaying output
print("\n=== MARKSHEET ===")
print("Subject 1:", a)
print("Subject 2:", b)
print("Subject 3:", c)
print("Subject 4:", d)
print("Subject 5:", e)
print("Total Marks:", total, "/ 500")
print("Percentage: {:.2f}%".format(percentage))
print("Grade:", grade)
print("Result:", result)