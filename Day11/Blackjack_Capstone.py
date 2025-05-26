"""
Blackjack Game (Console Version)

Description:
-------------
This is a simple, text-based implementation of the classic card game Blackjack (also known as 21).
The game is played between one player and the computer acting as the dealer.

Objective:
-------------
The goal of Blackjack is to beat the dealer's hand without exceeding 21.

How to Play:
-------------
- The player and dealer are each dealt two cards.
- The player can choose to:
    - "Hit" to draw another card.
    - "Stand" to end their turn and let the dealer play.
- The dealer must hit until their hand value is at least 17.
- Cards 2 through 10 are worth their face value.
- Face cards (Jack, Queen, King) are worth 10.
- Aces are worth 1 or 11, whichever is more favorable to the hand.
- If the player’s hand exceeds 21, they bust and lose automatically.
- After the player stands, the dealer reveals their hand and plays.
- The winner is determined by whoever is closer to 21 without going over.

Enjoy the game!
"""

import random
from art import logo 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    return [random.choice(cards), random.choice(cards)]

def hit(hand):
    hand.append(random.choice(cards))

def calculate_total(hand):
    total = sum(hand)
    # Adjust Aces if total > 21
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

print("Welcome to the Blackjack Game!")
play = input("Wanna play? Type 'y' or 'n': ")

while play.lower() == 'y':
    print(logo)  
    player = deal_cards()
    dealer = deal_cards()
    player_turn = True
    dealer_turn = False

    print(f"Your cards: {player}, current score: {calculate_total(player)}")
    print(f"Dealer's first card: {dealer[0]}")

    player_total = calculate_total(player)
    dealer_total = calculate_total(dealer)

    # Initial Blackjack Check
    if player_total == 21 and dealer_total == 21:
        print("Both have Blackjack! It's a draw.")
    elif player_total == 21:
        print("Blackjack! You win!")
    elif dealer_total == 21:
        print(f"Dealer's cards: {dealer}")
        print("Dealer has Blackjack! You lose.")
    else:
        # Player turn
        while player_turn:
            choice = input("Type 'y' to get another card, type 'n' to stand: ").lower()
            if choice == 'y':
                hit(player)
                player_total = calculate_total(player)
                print(f"Your cards: {player}, current score: {player_total}")
                if player_total > 21:
                    print("You went over 21. You lose.")
                    player_turn = False
                    dealer_turn = False
            elif choice == 'n':
                player_turn = False
                dealer_turn = True

        # Dealer turn
        if dealer_turn:
            print(f"Dealer's cards: {dealer}, current score: {dealer_total}")
            while dealer_total < 17:
                hit(dealer)
                dealer_total = calculate_total(dealer)
                print(f"Dealer draws: {dealer}, current score: {dealer_total}")

            # Final Comparison
            print(f"Your final hand: {player}, final score: {player_total}")
            print(f"Dealer's final hand: {dealer}, final score: {dealer_total}")

            if dealer_total > 21:
                print("Dealer went over. You win!")
            elif player_total > dealer_total:
                print("You win!")
            elif dealer_total > player_total:
                print("Dealer wins!")
            else:
                print("It's a draw!")

    play = input("Do you want to play another round? Type 'y' or 'n': ")

print("Thanks for playing Blackjack!")
