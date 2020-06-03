bill_amount = 0
while bill_amount == 0:
    try:
        bill_amount = float(input("How much was the total bill?\n"))
    except ValueError:
        print('Oops! You did not give a valid number!')

service_level = input("How was your service? good, fair, or bad?\n")
tip = 0
if service_level == "good":
    tip = bill_amount * 0.2
elif service_level == "fair":
    tip = bill_amount * 0.15
elif service_level == "bad":
    tip = bill_amount * 0.1
else:
    tip = float(input("Please enter a specific amount!"))
total = bill_amount + tip
print("Tip Amount: %s " % tip)
print("Total Amount: %s: " % total)

try:
    people = int(input("How many people to split bill with?\n"))
    if people == 0:
        people = 1
except ValueError:
    people = 1
    print("Invalid number.  Assumes 1")

split_amount = total/people

print("The amount for each individual is: %s" % split_amount)
