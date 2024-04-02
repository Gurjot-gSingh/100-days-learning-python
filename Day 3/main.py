print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("Welcome to the treasure island\n"
      "your mission is to find the treasure chest.")
choice_1 = input("You are at a crossroad which way you want to go 'left' or 'right': ").lower()
if choice_1 == "left":
    choice_2 = input("you've came across a river would you like to wait or jump using rope at the trees : ").lower()
    if choice_2 == "wait":
        choice_3 = input("You have reached at the caste and 3 doors that leads to the hall which door would you choose: "
                         "red , green or yellow : ").lower()
        if choice_3 == "green":
            print("You have reached the treasure chest and you get to keep all the valuables. You won")
        elif choice_3 == "red":
            print("You have reached the treasure but shot by the demon general and you died : ")
        else:
            print("You fell in the trap and died as spikes pierce through you")
    else:
        print("you tried to jump but slipped and fell into the river full of crocodiles. ")
else:
    print("you turned right and encounter a dragon that became your end.")


