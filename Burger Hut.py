import sys

#Starting
Name=str(input("Name: "))
Mobile_Number=int(input("Mobile Number: "))
print()
print("Hi!",Name,"Welcome to SS Burgers™ ")
print()
print()
print("                                                                                                                   |\ /|/| /|     ")            
print("                                                                                                                 |\||-|\||-/|/|   ")
print("  _______  _______      ______            _______  _______  _______  _______  _______                             \|\|//||////    ")
print(" (  ____ \(  ____ \    (  ___ \ |\     /|(  ____ )(  ____ \(  ____ \(  ____ )(  ____ \           _..----.._       |\/\||//||||    ")
print(" | (    \/| (    \/    | (   ) )| )   ( || (    )|| (    \/| (    \/| (    )|| (    \/         .'     o    '.     |||\\|/\\'||    ")
print(" | (_____ | (_____     | (__/ / | |   | || (____)|| |      | (__    | (____)|| (_____         /   o       o  \    |/'./\_/.'.|    ")
print(" (_____  )(_____  )    |  __ (  | |   | ||     __)| | ____ |  __)   |     __)(_____  )       |o        o     o|   |          |    ")
print("       ) |      ) |    | (  \ \ | |   | || (\ (   | | \_  )| (      | (\ (         ) |       /'-.._o     __.-'\   |    SS    |    ")
print(" /\____) |/\____) |    | )___) )| (___) || ) \ \__| (___) || (____/\| ) \ \__/\____) |       \      `````     /   | Burgers™ |    ")
print(" \_______)\_______)    |/ \___/ (_______)|/   \__/(_______)(_______/|/   \__/\_______)       |``--........--'`|    '.______.'     ")
print("                                                                                              \              /                    ")
print("                                                                                               `'----------'`                     ") 
print()
print()
Burgers=int(input("How many Burger(s) would you like to have:(MAX 9): "))

#Kitne burger mangwau?
if (0>=Burgers>=10):
    sys.exit()
elif (0<Burgers<10):
    print()
    print("Meal is for ₹399.")
    print("Burger is for ₹250")
    print()
    Meal=str(input("Would you like to make it a meal: ")).capitalize

    #Yaha se Meal option shuru hota hai
    if (Meal.startswith("Y")==True):
        print()
        FF=str(input("Would you like to take French Fires or Veg Fries: ")).capitalize

        # Yaha se fries ka option shuru
        if (FF.startswith('F') or FF.startswith('V'))==True:
            print()
            Cold_Drink=str(input("Would you like to take Coke or Sprite: ")).capitalize

            # Yaha se Cold Drink ki option shuru hoti hai
            if (Cold_Drink.startswith("C") or Cold_Drink.startswith("S"))==True:
                print()
                print("Thank you for choosing SS Burgers™! Here is your Bill. ")
                Meal=Burgers*399
                GST=(18/100)
                TAX=((Burgers*399)*GST)
                Total=(Burgers*399)+TAX
                print(" _________________________________________  ")
                print("|                SS Burgers™              | ")
                print("|                   BILL                  | ")
                print("|_________________________________________| ")
                print("|                    |                    | ")
                print("|       ITEMS        |       PRICE        | ")
                print("|____________________|____________________| ")
                print("|                                         | ")
                print("|                                         | ")
                print("|     ",Burgers,"Meal(s)            ₹",Meal  )
                print("|                                         | ")
                print("|        TAX                ₹",TAX,"        ")
                print("|                           _________     | ")
                print("|                                         | ")
                print("|        Total             ₹",Total          )
                print("|                                         | ")
                print("|_________________________________________| ")
                print("|         BILL Payed and Accepted         | ")
                print("|                                         | ")
                print("|    Thank you for choosing SS Burgers™   | ")
                print("|            Do Visit us Again            | ")
                print("|                                         | ")
                print("| Address: North Pochikin, Pub-G          | ")
                print("|                                         | ")
                print("|   We are not responsible for any kind   | ")
                print("|     of misshappening with Your Food.    | ")
                print("|                                         | ")
                print("|                                         | ")
                print("|          Eat at your OWN RISK!!         | ")
                print("|_________________________________________| ")

            #Exit for Cold Drink
            elif (Cold_Drink.startswith("C") or Cold_Drink.startswith("S"))==False:
                print('Invalid Input!!')
                exit()
        #Exit for Fries        
        elif (FF.startswith('F') or FF.startswith('V'))==False:
            print('Invalid Input!!')
            exit()
               
    #Yaha se No Meal option shuru hota hai
    elif (Meal.startswith("N")==True):
        print()
        print("Thank you for choosing SS Burgers™! Here is your Bill. ")
        Meal=Burgers*250
        GST=(18/100)
        TAX=((Burgers*250)*GST)
        Total=(Burgers*250)+TAX
        print(" _________________________________________  ")
        print("|                SS Burgers™              | ")
        print("|                   BILL                  | ")
        print("|_________________________________________| ")
        print("|                    |                    | ")
        print("|       ITEMS        |       PRICE        | ")
        print("|____________________|____________________| ")
        print("|                                         | ")
        print("|                                         | ")
        print("|     ",Burgers,"Burgers(s)         ₹",Meal  )
        print("|                                         | ")
        print("|        TAX                ₹",TAX,"        ")
        print("|                           _________     | ")
        print("|                                         | ")
        print("|        Total             ₹",Total          )
        print("|                                         | ")
        print("|_________________________________________| ")
        print("|         BILL Payed and Accepted         | ")
        print("|                                         | ")
        print("|    Thank you for choosing SS Burgers™   | ")
        print("|            Do Visit us Again            | ")
        print("|                                         | ")
        print("| Ph: 99887xxxxx                          | ")
        print("| Address: North Pochikin, Pub-G          | ")
        print("|                                         | ")
        print("|   We are not responsible for any kind   | ")
        print("|     of misshappening with Your Food.    | ")
        print("|                                         | ")
        print("|                                         | ")
        print("|          Eat at your OWN RISK!!         | ")
        print("|_________________________________________| ")
        print()

    #Exit for Meal option
    elif (Meal.startswith("Y") or Meal.startswith("N"))==False:
        print('Invalid Input!!')
        exit()

print()
print()

#Restart the program




