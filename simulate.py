from play import get_remaining_deck, play_game
from tqdm import tqdm

def simulate(num_players, hole, community, n=1000):
    seen_cards = hole+community
    deck = get_remaining_deck(seen_cards)

    wins = 0
    for i in tqdm(range(n)):
        if play_game(num_players, hole, community, deck):
            wins += 1
    return wins/n
