from enum import Enum
from random import randint

class Choose(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class RPSEngine:
    ALL_PLAYS = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
    UNFAIR_PLAYS = ['paper', 'scissors', 'rock']
    OPTIONS = ['paper', 'scissors', 'rock']

    def __init__(self):
        pass

    def evaluate(self, hplay, cpplay):
        game_result = RPSEngine.ALL_PLAYS[cpplay][hplay]
        if game_result == 0:
            print("There is a draw ({})".format(Choose(cpplay).name.lower()))
        elif game_result == 1:
            print("Well done. The computer chose {} and failed!".format(Choose(cpplay).name.lower()))
        elif game_result == 2:
            print("Sorry, but the computer chose {}".format(Choose(cpplay).name.lower()))

    def start_game(self):
        human_choice = self.human_play()
        cpu_choice = self.cpu_play(human_choice)
        self.evaluate(human_choice, cpu_choice)

    def human_play(self):
        choice = input()
        return Choose[choice.upper()].value if choice in RPSEngine.OPTIONS else None

    def cpu_play(self, human_choice):
        choice = randint(0, 2)
        return choice

# if __name__ == '__main__':
#     to testing
