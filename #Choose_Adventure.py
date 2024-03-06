import time

name = input("Type your name: ")
print("\nWelcome", name, "to the adventure!\nGood luck ... \n")

time.sleep(1.5)
def main():
    dead = False
    

    answer = input(
    "\nYou come to an end of a dirt road. You can go left or right. Which way do you want to go? \nType left or right  ").lower()

    # LEFT
    if answer == "left":
        answer = input("\nYou come to a river. You can walk around it, or swim across: \n Type: Swim or Walk ").lower()

    if answer == "swim":
        time.sleep(.5)
        print("Swimming...")
        time.sleep(.5)
        print("Swimming...")
        time.sleep(.5)
        print("Swimming...")
        time.sleep(1)
        print("Crunnchh!") 
        time.sleep(1)
        print("You were eaten by a hippo! Didn't know you were in Africa, did you?")
        time.sleep(1.3)

        dead = True
    elif answer == "walk":
        print("Walking ...")
        time.sleep(.6)
        print("Walking ...")
        time.sleep(.6)
        print("Walking ...")
        time.sleep(.6)
        print("Getting thristy ...")
        time.sleep(1.5)
        print("Getting thristier ...")
        time.sleep(2)
        print("You're dehydrated! ...", end='', flush=True)
        time.sleep(.5)
        print("......", end='', flush=True)
        time.sleep(.5)
        print("...........", end='', flush=True)
        time.sleep(.5)
        print("...................", end='', flush=True)
        dead = True
# RIGHT
    elif answer == "right":
        answer = input("\nYou come to a bridge. It looks wobbly, do you want to walk across it or jump off it?: \nType cross or jump ").lower()

    if answer == "jump":
        time.sleep(.3)
        print("You jumped and hit your head on the ground.")
        dead = True
    elif answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you want to talk to him?\nType yes or no  ")

        if answer == "yes":
            talk = input("You talked to the stranger and he directs you to the gas station. Walk to the gas station or insult his beard? \nType: walk or insult  ").lower()
            if talk == "walk":
                print("\nWalking ...")
                time.sleep(1.2)
                print("You arrived at the gas station. You only have enough money to buy either a Cliff Bar or a Razor scooter.")
                time.sleep(3)
                answer = input("Which do you want to buy? \nType: food or scooter")
                if answer == "food":
                    print("You are very hungry and scarf down the Cliff Bar")
                    time.sleep(.5)
                    print("Eating ...")
                    time.sleep(.5)
                    print("Eating ...")
                    time.sleep(1)
                    print("The Cliff Bar was expired! You puke all over the gas station floor...")
                    time.sleep(1)
                    print("Puking ...")
                    time.sleep(.2)
                    print("Puking ...")
                    time.sleep(.2)
                    print("Puking ...")
                    time.sleep(.2)
                    print("You died from puking!\n")
                    dead = True
                elif answer == "scooter":
                    print("You ride the razor scooter down the road")
                    time.sleep(.3)
                    print("Riding ...")
                    time.sleep(.4)
                    print("Riding ...")
                    time.sleep(.4)
                    print("Riding ...")
                    time.sleep(1)
                    print("You come across a large pile of cash!")
                    time.sleep(.7)
                    print("All of your problems go away!\n You Win! ")
                    print("__________ Game Over ___________")
                    exit()
            if talk == "no":
                time.sleep(1)
                print("Probably for the best.")
                time.sleep(1)
                print("The man did`t look too friendly.")
                time.sleep(.8)
                print("You see a gas station in the distance and walk to it.")
                time.sleep(2)
                print("You arrived at the gas station. You only have enough money to buy either a Cliff Bar or a Razor scooter.")
                time.sleep(3)
                answer = input("Which do you want to buy? \nType: food or scooter")
                if answer == "food":
                    print("You are very hungry and scarf down the Cliff Bar")
                    time.sleep(.5)
                    print("Eating ...")
                    time.sleep(.5)
                    print("Eating ...")
                    time.sleep(1)
                    print("The Cliff Bar was expired! You puke all over the gas station floor...")
                    time.sleep(1)
                    print("Puking ...")
                    time.sleep(.2)
                    print("Puking ...")
                    time.sleep(.2)
                    print("Puking ...")
                    time.sleep(.2)
                    print("You died from puking!\n")
                    dead = True
                elif answer == "scooter":
                    print("You ride the razor scooter down the road")
                    time.sleep(.3)
                    print("Riding ...")
                    time.sleep(.4)
                    print("Riding ...")
                    time.sleep(.4)
                    print("Riding ...")
                    time.sleep(1)
                    print("You come across a large pile of cash!")
                    time.sleep(.7)
                    print("All of your problems go away!\n You Win! ")
                    print("__________ Game Over ___________")
                    exit()
                            


            if talk == "insult":
                print("The man takes great pride in his beard, brushing and washing it every morning.")
                time.sleep(2.5)
                print("He is very offended and slaps you.")
                time.sleep(.5)
                print("\nUnfortunately for you, he won several bodybuilder slap competitions and you die from the impact...")
                print("Smackk! ...", end='', flush=True)
                time.sleep(1)
                print("......", end='', flush=True)
                time.sleep(1)
                print("............", end='', flush=True)
                time.sleep(1)
                print("......................", end='', flush=True)
                time.sleep(1)
                dead = True
      

    while dead == True:  # Dead player
        time.sleep(2)
        print("\nYou died! \nWelcome to the afterlife", name, ".")
        time.sleep(2.5)
        print("   _______")
        print("  /       \\")
        print(" |  O   O  |")
        print(" |    ∆    |")
        print(" |   ___   |")
        print(" |  |   |  |")
        print("  \\_______/")

        time.sleep(1.2)
        answer = input("\n You are slowly sinking down into the ground, resist? ... \nType: resist or continue  ")
        if answer.lower() == "resist":
            print("Resisting ... ")
            time.sleep(2)
            print("Resisting ... ")
            time.sleep(2)
            print("You are starting to float up ...\n")
            time.sleep(1)
            print("Rising ...")
            time.sleep(.5)
            print("Rising ...")
            time.sleep(.5)
            print("Rising ...")
            time.sleep(.5)
            print("You reach the clouds. Pretty nice up here aint it?\n")
            time.sleep(1.5)
            answer = input("A big shining light asks you if you ate your vegetables... did you?  \nType yes or no ").lower()
            if answer == "yes":
                time.sleep(.9)
                print("Swag.")
                time.sleep(2)
                print("The ball of light gives you another chance . . . ")
                time.sleep(2.5)
                print("Good thing you ate your broccoli.")
                time.sleep(1)
                print("Reincarnating ...")
                time.sleep(.4)
                print("Reincarnating ...")
                time.sleep(.4)
                print("Reincarnating ...")
                time.sleep(1)
                print("Time traveling to the end of the road ...\n\n")
                time.sleep(3)
                main()

            elif answer == "no":
                print("Uh oh ... ")
                time.sleep(2)
                print("Back down you go.")
                print("| | | |")
                time.sleep(0.5)
                print("| | | |")
                time.sleep(0.5)
                print("| | | |")
                time.sleep(0.5)
                print("| | | |")
                time.sleep(0.5)
                print("| | | |")
                time.sleep(0.5)
                print("| | | |")
                time.sleep(0.5)
                print("| | | |")
                time.sleep(0.5)
                print("| | | |")
                print("________\n")
                print("Thump! You hit the ground.")
        if answer == "continue":
            print("Sinking ...")
            time.sleep(.5)
            print("Sinking ...")
            time.sleep(.5)
            print("Sinking ...")
            time.sleep(.5)
            print("Your soul fell into Earth's Core and melted ...")
            time.sleep(.8)
            print("You Lose.")
            print("_________ Game Over _________")
            quit()
    else:
        print("Not valid. Game over.")  # Error
main()