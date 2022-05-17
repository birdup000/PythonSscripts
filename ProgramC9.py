daynumber = 0
askmilage = int (input("How many miles did you travel day"))
Answer = input('Want to see the milage ?')
tmiles = 0
Milage = 0
while Answer == 'yes' or Answer == 'y':
   
    print("The program will give you or team milage number",askmilage,"degrees" )
    if (Milage > 1 ): 
        Milage == tmiles
        print("here's your Milage")
    elif (Milage > 1 ):
        print("Your team miles is", tmiles)
    else:
        print("Would you like to add more team data?") 
    daynumber = daynumber + 1
    Answer = int(input("How many team miles were ran?"))
print('Have a great day!')