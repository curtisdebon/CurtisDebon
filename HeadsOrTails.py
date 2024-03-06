import random

play = input("Do you want to play? ")

chip_count = 0
buy_in = 0
sides = ["heads", "tails"]
player_in = True
wins = 0

if play.lower() == "yes":
    buy_in = input("How much do you want to deposit __  ")
    if buy_in.isdigit():
        buy_in = int(buy_in)
        chip_count += buy_in
    print("You have", chip_count, "chips.")

while player_in:
    place_bet = input("\nType your bet or Q to quit  ")

    if place_bet.lower() == "q":
        quit()

    if place_bet.isdigit():
        place_bet = int(place_bet)

    if chip_count <= 0:
        print("You ran out of chips!")
        break

    user_pick = input("\nPick heads or tails __  ")

    # Check if the user input is valid
    while user_pick.lower() not in sides:
        print("Invalid input! Please enter 'heads' or 'tails'.")
        user_pick = input("\nPick heads or tails __  ")

    computer_pick = random.choice(sides)

    if computer_pick == user_pick.lower():
        print("You win!")
        chip_count += place_bet
        wins += 1
        print("You now have", chip_count, "chips.")
    else:
        print("\nYou lost! The coin landed on", computer_pick, "!")
        chip_count -= place_bet
        print("You now have", chip_count, "chips.")

print("Game over. You ended up with", chip_count, "and won", wins, 'times.')
