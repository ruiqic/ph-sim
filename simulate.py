import numpy as np
from play import get_remaining_deck, play_game
from constants import CARDS
from tqdm import tqdm

def simulate(num_players, hole, community, n=1000):
    seen_cards = hole+community
    deck = get_remaining_deck(seen_cards)

    wins = np.zeros(num_players-1)
    for i in tqdm(range(n)):
        wins = wins + play_game(num_players, hole, community, deck)
    return wins/n

def get_num_players():
    while True:
        user_input = input("Enter number of players: ")
        if user_input == "new" or user_input == "reset":
            return user_input
        try:
            number = int(user_input)
            if number < 2:
                print("Invalid number of players")
                raise ValueError
            return number
        except ValueError:
            pass

def get_cards(num_cards, stage, seen_cards):
    while True:
        user_input = input(f"Enter {stage} cards : ")
        if user_input == "new" or user_input == "reset":
            return user_input
        try:
            cards = user_input.upper().replace("10", "T").split(" ")
            if len(cards) not in num_cards:
                print("Invalid input: invalid number of cards")
                raise ValueError
            for card in cards:
                if card not in CARDS:
                    print("Invalid input: invalid card")
                    raise ValueError
            if len(cards+seen_cards) != len(set(cards+seen_cards)):
                print("Invalid input: duplicate cards")
                raise ValueError
            return cards
        except ValueError:
            pass

def print_probabilities(prob):
    pure_random = np.round(1 / np.arange(2,len(prob)+2) * 100, 2)
    pretty_prob = np.round(prob * 100, 2)
    probs_text = []
    random_text = []
    for i in range(len(pretty_prob)):
        probs_text.append(f"{i+2}: {pretty_prob[i]:.2f}%")
        random_text.append(f"{i+2}: {pure_random[i]:.2f}%")
    print("Random: ", "; ".join(random_text))
    print("Equity: ", "; ".join(probs_text))
    

def main():
    while True:
        print("----------------------------- New Game (red: ♦d, ♥h) (black: ♣c, ♠s) -----------------------------")
        
        num_players = get_num_players()
        if num_players is None:
            continue
        while True:
            community = []
            hole = get_cards(num_cards=[2], stage="hole", seen_cards=[])
            if hole == "reset":
                break
            elif hole == "new":
                continue
            print("Simulating preflop", hole, community)
            prob = simulate(num_players, hole, community, n=50000)
            print_probabilities(prob)
            
            flop = get_cards(num_cards=[3,4,5], stage="flop", seen_cards=hole)
            if flop == "reset":
                break
            elif flop == "new":
                continue
            community += flop
            print("Simulating flop", hole, community)
            prob = simulate(num_players, hole, community, n=50000)
            print_probabilities(prob)

            if len(community) == 3:
                turn = get_cards(num_cards=[1,2], stage="turn", seen_cards=hole+community)
                if turn == "reset":
                    break
                elif turn == "new":
                    continue
                community += turn
                print("Simulating turn", hole, community)
                prob = simulate(num_players, hole, community, n=50000)
                print_probabilities(prob)

            if len(community) == 4:
                river = get_cards(num_cards=[1], stage="river", seen_cards=hole+community)
                if river == "reset":
                    break
                elif river == "new":
                    continue
                community += river
                print("Simulating river", hole, community)
                prob = simulate(num_players, hole, community, n=50000)
                print_probabilities(prob)
        
if __name__ == "__main__":
    main()
