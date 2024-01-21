Poker Hand Simulator
=====
A very fast poker odds calculator. Estimates the probability of winning given the available information (hole cards and community cards) in a poker game. The estimation leverages a [perfect hash algorithm](https://github.com/HenryRLee/PokerHandEvaluator/blob/master/Documentation/Algorithm.md) to run simulations efficiently.

## Requirements
Simulations use [phevaluator](https://github.com/HenryRLee/PokerHandEvaluator) and the progress bar uses `tqdm`.

## Usage
To run
```
python simulate.py
```
Next, enter the number of players and cards when prompted to run simulations.
<pre>
Enter number of players: <b>8</b>
----------------------------- New Game (red: ♦d, ♥h) (black: ♣c, ♠s) -----------------------------
Enter hole cards : <b>Ad aC</b>
Simulating preflop ['AD', 'AC'] []
100%|██████████████████████████████████████████████████████| 50000/50000 [00:02<00:00, 18751.59it/s]
Random:  2: 50.00%; 3: 33.33%; 4: 25.00%; 5: 20.00%; 6: 16.67%; 7: 14.29%; 8: 12.50%
Equity:  2: 85.68%; 3: 74.06%; 4: 64.32%; 5: 56.50%; 6: 49.78%; 7: 44.17%; 8: 39.53%
Enter flop cards : <b>10h ts js</b>
Simulating flop ['AD', 'AC'] ['TH', 'TS', 'JS']
100%|██████████████████████████████████████████████████████| 50000/50000 [00:02<00:00, 19017.23it/s]
Random:  2: 50.00%; 3: 33.33%; 4: 25.00%; 5: 20.00%; 6: 16.67%; 7: 14.29%; 8: 12.50%
Equity:  2: 83.79%; 3: 70.61%; 4: 60.09%; 5: 51.55%; 6: 44.64%; 7: 38.89%; 8: 33.89%
Enter turn cards : <b>8c</b>
Simulating turn ['AD', 'AC'] ['TH', 'TS', 'JS', '8C']
100%|██████████████████████████████████████████████████████| 50000/50000 [00:02<00:00, 19255.32it/s]
Random:  2: 50.00%; 3: 33.33%; 4: 25.00%; 5: 20.00%; 6: 16.67%; 7: 14.29%; 8: 12.50%
Equity:  2: 81.36%; 3: 66.54%; 4: 54.81%; 5: 45.21%; 6: 37.52%; 7: 31.57%; 8: 26.46%
Enter river cards : <b>3s</b>
Simulating river ['AD', 'AC'] ['TH', 'TS', 'JS', '8C', '3S']
100%|██████████████████████████████████████████████████████| 50000/50000 [00:02<00:00, 17676.09it/s]
Random:  2: 50.00%; 3: 33.33%; 4: 25.00%; 5: 20.00%; 6: 16.67%; 7: 14.29%; 8: 12.50%
Equity:  2: 82.62%; 3: 67.84%; 4: 55.51%; 5: 45.18%; 6: 36.26%; 7: 29.13%; 8: 23.03%
</pre>

For any prompt, enter `new` to start a new round or `reset` to start a new game with a different number of players.
