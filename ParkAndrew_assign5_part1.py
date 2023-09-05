"""
Assignment #5, Part 1
Andrew Park
"""


budget = float(input("Enter budget for your party: "))
slice = float(input("Cost per slice of pizza: "))
pie = float(input("Cost per whole pizza pie (8 slices): "))
people = int(input("How many people will be attending your party? "))
total = 0
for i in range(1, (people+1)):
    eat = int(input("Enter number of slices for person #"+ str(i) + ": " ))
    if eat > 0:
        total += eat
    else:
        total -= eat
        while eat < 0:
            print("Not a valid entry, try again")
            eat = int(input("Enter number of slices for person #"+ str(i) + ": "))

print()

if total > 8:
    pies = total // 8
    leftover = (total - (pies * 8))
elif total == 8:
    pies = 1
    leftover = 0
else:
    leftover = total
    pies = 0

cost = format((pies * pie) + (leftover * slice), ".2f")
left1 = (budget - float(cost))
left2 = abs(left1)
left = format(left2, ".2f")

if left1 < 0:
    print("Your order cannot be completed")
    print("You would need to purchase", pies, "pies and", leftover, "slices")
    print("This would put you over budget by", left)
elif left1 == 0:
    print("You should purchase", pies, "pies and", leftover, "slices")
    print("Your total cost wil be:", cost)
    print("You will have no money left after your order.")
else:
    print("You should purchase", pies, "pies and", leftover, "slices")
    print("Your total cost wil be:", cost)
    print("You will still have", left, "left after your order")









