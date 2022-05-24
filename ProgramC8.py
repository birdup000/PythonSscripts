item1str = input('Name of item1?')
item1 = int(input("What's item1 price?"))




item2str = input('Name of item2?')
item2 = int(input("What's item2 price?"))


item3str = input('Name of item3?')
item3 = int(input("What's item3 price?"))

itemtotalcost = item3 + item2 + item1
 
tax = itemtotalcost * 0.07 
finalcost = itemtotalcost + tax
print("Your total cost is $",finalcost)

budgetcost = 500 - finalcost

if budgetcost < 0:
    print("You are this much over$",budgetcost)

if budgetcost >= 0:
    print("You have this amount left over$",budgetcost)