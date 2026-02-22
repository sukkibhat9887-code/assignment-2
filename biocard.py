# Variables for student details
name = input("Enter your name:")
age = int(input("Enter the age:"))
course = input("Enter your course:")
college = input("Enter your college:")
email = input("Enter your email:")

# Printing Bio Card
print("|============================================|")
print("|              STUDENT BIO CARD              |")
print("|============================================|")
print("| Name    : {:<30}   |".format(name))
print("| Age     : {:<30}   |".format(str(age) + " years"))
print("| Course  : {:<30}   |".format(course))
print("| College : {:<30}   |".format(college))
print("| Email   : {:<30}   |".format(email))
print("|============================================|")