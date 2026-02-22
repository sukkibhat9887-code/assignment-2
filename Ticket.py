age = int(input("Enter age: ")) #Input
day = input("Enter day of week: ").lower()
tickets = int(input("Enter number of tickets: "))

# Determine base price based on age
if age < 3:
    base_price = 0
    category = "Free"
elif 3 <= age <= 12:
    base_price = 150
    category = "Child"
elif 13 <= age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# Calculate subtotal
subtotal = base_price * tickets

# Check discount
if day in ["friday", "saturday", "sunday"]:
    discount = subtotal * 0.20
else:
    discount = 0

# Final calculations
price_after_discount = subtotal - discount

# Output
print("\n=== MOVIE TICKET BILL ===")
print("Category:", category)
print("Base price per ticket: ₹", base_price)
print("Subtotal: ₹", subtotal)
print("Discount: ₹", discount)
print("Price after discount: ₹", price_after_discount)
print("Total amount to pay: ₹", price_after_discount)