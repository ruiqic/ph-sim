from play import get_remaining_deck, play_game
from constants import CARDS
from tqdm import tqdm

def simulate(num_players, hole, community, n=1000):
    seen_cards = hole+community
    deck = get_remaining_deck(seen_cards)

    wins = 0
    for i in tqdm(range(n)):
        if play_game(num_players, hole, community, deck):
            wins += 1
    return wins/n

def get_num_players():
    while True:
        user_input = input("Enter number of players: ")
        if user_input == "new":
            return None
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
        if user_input == "new":
            return None
        try:
            cards = user_input.split(" ")
            if len(cards) != num_cards:
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
            

def main():
    while True:
        print("----------------------------- New Game (red: ♦d, ♥h) (black: ♣c, ♠s) -----------------------------")
        community = []
        num_players = get_num_players()
        if num_players is None:
            continue
        
        hole = get_cards(num_cards=2, stage="hole", seen_cards=[])
        if hole is None:
            continue
        print("Simulating preflop", hole, community)
        prob = simulate(num_players, hole, community, n=100000)
        print(f"Preflop equity = {prob*100:.2f}%")

        flop = get_cards(num_cards=3, stage="flop", seen_cards=hole)
        if flop is None:
            continue
        community += flop
        print("Simulating flop", hole, community)
        prob = simulate(num_players, hole, community, n=100000)
        print(f"Flop equity = {prob*100:.2f}%")

        turn = get_cards(num_cards=1, stage="turn", seen_cards=hole+community)
        if turn is None:
            continue
        community += turn
        print("Simulating turn", hole, community)
        prob = simulate(num_players, hole, community, n=100000)
        print(f"Turn equity = {prob*100:.2f}%")

        river = get_cards(num_cards=1, stage="river", seen_cards=hole+community)
        if river is None:
            continue
        community += river
        print("Simulating river", hole, community)
        prob = simulate(num_players, hole, community, n=100000)
        print(f"River equity = {prob*100:.2f}%")
        
if __name__ == "__main__":
    main()
