# JAMES MOSETI MOTURI
# SCT211-0095/2022

total_bill = float(input("Enter the total bill amount: $"))

while True:
    tip_percentage = input("Enter the tip percentage (10, 12, or 15): ")
    if tip_percentage in ["10", "12", "15"]:
        break
    else:
        print("Invalid input. Please enter 10, 12, or 15 for tip percentage.")

num_people = int(input("Enter the number of people splitting the bill: "))

tip_percentage = float(tip_percentage)
tip_amount = (tip_percentage / 100) * total_bill

total_amount = total_bill + tip_amount

amount_per_person = total_amount / num_people

print(f"Each person should pay: ${amount_per_person:.2f}")
