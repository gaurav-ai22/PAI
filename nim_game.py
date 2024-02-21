import random
from functools import reduce

COMPUTER, HUMAN = 1, 2

class Move:
    def __init__(self, pile_index=0, stones_removed=0):
        self.pile_index, self.stones_removed = pile_index, stones_removed

def show_piles(p): print("Current Game Status ->", *p)

def game_over(p): return all(x == 0 for x in p)

def declare_winner(w): print(f"\n{'HUMAN' if w == COMPUTER else 'COMPUTER'} won")

def calculate_nim_sum(p): return reduce(lambda x, y: x ^ y, p)

def make_move(p, m):
    s, nim_sum = p[m.pile_index], calculate_nim_sum(p)
    m.pile_index = next((i for i, x in enumerate(p) if (x ^ nim_sum) < x), random.choice([i for i, x in enumerate(p) if x > 0]))
    m.stones_removed = min(random.randint(1, p[m.pile_index]), p[m.pile_index])
    p[m.pile_index] -= m.stones_removed

def play_game(p, w):
    print("\nGAME STARTS")
    m = Move()
    while not game_over(p):
        show_piles(p)
        make_move(p, m)
        print(f"{'COMPUTER' if w == COMPUTER else 'HUMAN'} removes {m.stones_removed} stones from pile at index {m.pile_index}")
        w = HUMAN if w == COMPUTER else COMPUTER
    show_piles(p)
    declare_winner(w)

def know_winner_before_playing(p, w): print(f"Prediction before playing the game -> {'COMPUTER' if calculate_nim_sum(p) != 0 else 'HUMAN'} will win")

# Test Case
p = [3, 4, 5]
know_winner_before_playing(p, COMPUTER)
play_game(p, COMPUTER)
