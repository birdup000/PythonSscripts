name = input("What is your name? ")
itemname = input("What is the name of the item? ")
priceofitem = int(input("What is your item price? "))
tax=0.07*priceofitem
total=tax+priceofitem
print("This is your item price. $",total)