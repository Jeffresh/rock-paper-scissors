from enum import Enum


class Choose(Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2


class RPSEngine:
    ALL_PLAYS = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
    UNFAIR_PLAYS = ['paper', 'scissors', 'rock']
    OPTIONS = ['paper', 'scissors', 'rock']

    def __init__(self):
        pass

    def start_game(self):
        pass

    def human_play(self):
        choice = input()
        return choice if choice in RPSEngine.OPTIONS else None

    def cpu_play(self):
        pass
