print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = tip / 100 * bill
total_bill = bill + tip_amount
amount_per_person = total_bill / people
final_amount = round(amount_per_person, 2)
print(f"Each person should pay: ${final_amount}")