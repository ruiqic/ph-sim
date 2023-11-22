import random
from constants import RANKS, SUITS

def get_remaining_deck(seen_cards):
    known_cards = set(seen_cards)
    remaining_deck = []
    for rank in RANKS:
        for suit in SUITS:
            card = rank + suit
            if card not in known_cards:
                remaining_deck.append(card)
    return remaining_deck

def deal_cards(deck, num_other_players, community):
    num_cards_needed_community = 5-len(table)
    num_cards_needed_dealt = num_other_players * 2
    num_cards_needed = num_cards_needed_community + num_cards_needed_dealt

    cards = random.sample(deck, k=num_cards_needed)
    players = []
    i = 0
    for j in range(num_other_players):
        players.append(cards[i:i+2])
        i += 2
    filled_community = community + cards[i:]
    return filled_community, players

def play_game(num_players, hole, community, deck, verbose=False):
    # return True for win or draw
    filled_community, players = deal_cards(deck, num_players-1, community)
    if verbose:
        print("Community:", filled_community)
        print("My hand:", hole)
        for i in range(num_players-1):
            print(f"Player {i} hand:", players[i])
        
    my_hand = filled_community + hole
    player_hands = [filled_community + player for player in players]

    my_score = evaluate_cards(*my_hand)
    player_scores = [evaluate_cards(*player_hand) for player_hand in player_hands]

    return my_score >= max(player_scores)