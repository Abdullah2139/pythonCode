print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")

choice1 = input("You're at a crossroad. Do you want to go left or right? ").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'swim' to swim across or 'wait' to wait for a boat. ").lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed.")
        choice3 = input("There is a house with three doors. One red, one yellow, and one blue. Which color do you choose? ").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
    else:
        print("You get attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")