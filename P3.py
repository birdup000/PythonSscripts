
Answer = input('Want to see the recomennded activity for the temp?')

while Answer == 'yes' or Answer == 'y':

    tempask = int(input("What is the temp outside?"))
    print("The program will list you your options for",tempask,"degrees" )
    if (tempask >= 80 ): 
        print("Go to the beach")
    elif (tempask >= 10 and tempask <=30):
        print("Go skiing")
    else:
        print("Stay Home") 
    Answer = input('Want to see the recomennded activity for the temp?') 
print('Have a great day!')