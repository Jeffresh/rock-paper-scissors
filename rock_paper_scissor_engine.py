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
        self.rating_file = open('rating.txt', mode='a')
        self.actual_user = None
        self.actual_user_score = 0
        self.rating_file.close()

    def evaluate(self, hplay, cpplay):
        game_result = RPSEngine.ALL_PLAYS[cpplay][hplay]
        if game_result == 0:
            print("There is a draw ({})".format(Choose(cpplay).name.lower()))
            self.actual_user_score += 50
        elif game_result == 1:
            print("Well done. The computer chose {} and failed!".format(Choose(cpplay).name.lower()))
            self.actual_user_score += 100
        elif game_result == 2:
            print("Sorry, but the computer chose {}".format(Choose(cpplay).name.lower()))

    def start_game(self):
        input_choice = input()
        while input_choice in RPSEngine.OPTIONS:
            human_choice = self.human_play(input_choice)
            cpu_choice = self.cpu_play(human_choice)
            self.evaluate(human_choice, cpu_choice)
            input_choice = input()
        else:
            if input_choice == '!exit':
                print("Bye!")
            else:
                print("Invalid input")

    def register_name(self, user_name):
        previous_player = False
        self.rating_file = open('rating.txt', mode='r+')

        for line in self.rating_file:
            name, rate = line.split()
            if name == user_name:
                self.actual_user_score = int(rate)
                previous_player = True
                break
        if not previous_player:
            self.rating_file.write('{} 0\n'.format(user_name))
        self.rating_file.close()

    def new_game(self):
        name = input('Enter your name: ')
        print('Hello, {}'.format(name))
        self.register_name(name)

    def human_play(self, choice):
        return Choose[choice.upper()].value if choice in RPSEngine.OPTIONS else None

    def cpu_play(self, human_choice):
        choice = randint(0, 2)
        return choice

# if __name__ == '__main__':
#     rps_game = RPSEngine()
#     rps_game.start_game()
