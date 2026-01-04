# ASCII art : https://ascii.co.uk/art/treasure

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross_road_choice = input("There is a crossroad in front of you. Do you want to wait or cross the road ?\n\tType wait or cross: ").lower()

if cross_road_choice == "cross":
    print("Great choice, Now there's a river in front of you.\n")
    river_choice = input("Do you want to wait for the boat or swim?\n\tType wait or swim: ").lower()

    if river_choice == "wait":
        print("That's clever not to swim in a river full of crocodiles eh.!\n")
        print("Finally you are now one step away from the treasure.! Choose wisely.!")

        door_choice = input("There are 3 doors in front of you.!Red , Green and Yellow.!\n\tChoose one: ").lower()

        if door_choice == "red":
            print("Holla..!! You are rich.! You found the treasure you were looking for.!.\nThank You for playing this Game.! See you next time champ.!")
        elif door_choice == "yellow":
            print("Hahahaha..!! You died .! The room was full of snakes.!\nGame Over.!")
        elif door_choice == "green":
            print("Look back.! Boom.!! It was a knife trap and you fell for it.!\nGame Over.! ")
        else:
            print("What's the purpose of choosing a door which is not there.! Go back hush.! \nGame Over.!")

    elif river_choice == "swim":
        print("Are you blind ? Who swims in a river full of crocodile. Now go away it's dinner time for the crocodiles.!\nGame Over.!")

    else:
        print("When there are only two options. What's the purpose of choosing something else.?\nGame Over.!")

elif cross_road_choice == "wait":
    print("Oops wrong choice there.!\nSomeone else took the treasure while you kept waiting.!\nGame Over.!")

else:
    print("Invalid Input.\nGame Over.!")