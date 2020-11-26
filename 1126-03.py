direction = input("left or right? ")

if direction == "left":
    swim_wait = input("swim or wait? ")
    if swim_wait == "wait":
        door = input("red, blue, yellow or anything else ")
        if door == "red":
            print("Burned by fire. Game over.")
        elif door == "blue":
            print("Eaten by beasts. Game over.")
        elif door == "yellow":
            print("You win!")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over. ")
