from enum import Enum


class Choose(Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2


class RPSEngine:
    all_plays = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
    unfair_plays = ['paper', 'scissors', 'rock']

    def __init__(self):
        pass

    def start_game(self):
        pass

    def human_play(self):
        pass

    def cpu_play(self):
        pass
