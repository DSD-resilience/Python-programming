import random

  """"No aces, no betting.""""

def draw_card():
    """Returns a random card value between 1 and 11."""
    return random.randint(1, 11)

# Player Turn
player_total = 0
while True:
    card = draw_card()
    player_total += card
    print(f"You drew a {card}. Total: {player_total}")

    if player_total > 21:
        print("You busted! 💥 Dealer wins.")
        break

    choice = input("Do you want to hit or stay? (hit/stay): ").lower()
    if choice == "stay":
        break

# Dealer Turn
if player_total <= 21:
    dealer_total = 0
    print("\nDealer's turn:")
    while dealer_total < 17:
        card = draw_card()
        dealer_total += card
        print(f"Dealer drew a {card}. Total: {dealer_total}")
        if dealer_total > 21:
            print("Dealer busted! 💥 You win.")
            break

    if dealer_total <= 21:
        print("\nFinal Results:")
        print(f"Your total: {player_total}")
        print(f"Dealer's total: {dealer_total}")
        if player_total > dealer_total:
            print("You win! 🏆")
        elif player_total < dealer_total:
            print("Dealer wins! 🃏")
        else:
            print("It's a tie! 🤝")
