name = input("Type your name: ")
print("Welcome", name , "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go right or left. Which way would you like to go?: ").lower()

if answer == "left":
    answer == input("You came to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer=="walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("No valid option. You lose.")

elif answer == "right":
    if answer == "right":
        answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)").lower()

    if answer == "back":
        print("You go back, you lose.")
    elif answer=="cross":
        answer == input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no)").lower()
        if answer == "yes":
            print("You talk to a stranger and they give you gold. YOU WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. you lose.")
        else:
            print("No valid option. You lose.")
    else:
        print("No valid option. You lose.")

else:
    print("No valid option. You lose.")

print("Thank you for trying", name)
