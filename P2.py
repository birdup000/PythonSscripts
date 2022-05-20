feet = int(input("How many feet are you away from the person in front of you? "))
mask = input("Are you wearing a mask?")
while mask == 'yes' or mask == 'y' and feet>=6:
       print("You are safe. But please still wear your mask and continue to stand 6 feet away from the person in front of you.")
       quit()
while mask == 'yes' or mask == 'y' and feet<6:
    print("You are not safe. So please stand 6 feet away from the person in front of you and continue to wear a mask.")
    quit()

        
while mask == 'no' or mask == 'n' and feet<6:
        print("You are not safe. So please wear a mask and stand 6 feet apart from the person in front of you.")
        quit()
while mask == 'no' or mask == 'n' and feet>=6:
        print("You are not safe. So please wear a mask and continue to stand 6 feet away.")
        quit()

