
# Taking inputs
tot_bill = float(input("Enter total bill: "))
peo = int(input("Number of people: "))
tax_per = float(input("Tax percentage: "))
tip_per = float(input("Tip percentage: "))

# Calculations
tax_amt = (tax_per / 100) * tot_bill
after_tax = tot_bill + tax_amt
tip_amt = (tip_per / 100) * after_tax
fin_tot = after_tax + tip_amt
per_person = fin_tot / peo

# Displaying bill breakdown
print("=== BILL BREAKDOWN ===")
print(f"Subtotal: ₹{tot_bill:.2f}")
print(f"Tax ({tax_per}%): ₹{tax_amt:.2f}")
print(f"After tax: ₹{after_tax:.2f}")
print(f"Tip ({tip_per}%): ₹{tip_amt:.2f}")
print(f"Total: ₹{fin_tot:.2f}")
print(f"Per person: ₹{per_person:.2f}")