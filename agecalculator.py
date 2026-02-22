
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))

age = current_year - birth_year #calculate age

leap_years = age // 4
total_days = age * 365 + leap_years # More accurate days calculation (including leap years)

hours = total_days * 24 # Convert to hours and minutes
minutes = hours * 60

print("Current Age:", age, "years") #output
print("Age in Days:", total_days)
print("Age in Hours:", hours)
print("Age in Minutes:", minutes)
print("Years until 100:", 100 - age)