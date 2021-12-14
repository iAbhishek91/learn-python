print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
left_or_rigt = input("Left or Right?\n").lower()
if left_or_rigt == "left":
    swim_or_wait = input("Swim or Wait:\n").lower()
    if swim_or_wait == "wait":
        which_door = input("which door(Red,Blue,Yellow):\n").lower()
        if which_door == "yellow":
            print("You Win!")
        else:
            print("Game over!")
    else:
        print("Game over!")
else:
    print("Game over!")