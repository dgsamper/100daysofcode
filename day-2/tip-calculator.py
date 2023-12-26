# tip calculator

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?\n$"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people_split = int(input("How many people to split the bill?\n"))

result = (total_bill * (percentage_tip / 100) + total_bill) / people_split
result_formatted = "{:.2f}".format(result)

print(f"Each person should pay ${result_formatted}")