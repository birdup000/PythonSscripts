print("This program will get the sum price of all items you input into it.")
print("Type None as the name of an item to end the program.")
print("Type $0 as the price of an item to end the program.")
want_to_run_program = 'y'
while want_to_run_program == 'y':
    item_names = []
    item_prices = []
    want_to_add_items = 'y'
    while True:
        New_Name = input("What is the name of this item?")
        if New_Name == 'None':
            break
        else:
            item_names.append(New_Name)
        New_Price = float(input("What is the price of this item? (please don't use a $ symbol)"))
        New_Price = round(New_Price, 2)
        if New_Price == '0':
            item_prices.pop
            break
        else:
            item_prices.append(New_Price)
    allitems = item_names

    print("You purchased", allitems)
    allitemprices = sum(item_prices)
    print("These purchases cost a total of ${}.".format(allitemprices))
    want_to_add_items = input("Do you want to run this program again? (y/n).")
