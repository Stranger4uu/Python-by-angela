

print("Welcome to tip calculator :) ")
bill = float(input("What is the total bill ? : "))
tip = int(input("How much tip would you like to give 10,12,15 ? : "))
people = int(input("How many people to split the bill ? : "))
bill_with_tip = bill * (1 + tip / 100)
final_amount = round(bill_with_tip / people,2)
print(f"Amount to be paid : {final_amount}")