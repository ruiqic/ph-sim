import itertools
SUITS = ['D','S','C','H']
RANKS = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
CARDS = set([rank + suit for rank, suit in itertools.product(RANKS, SUITS)])