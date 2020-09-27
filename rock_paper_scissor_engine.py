from enum import Enum
from random import randint


class Choose(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class RPSEngine:
    OPTIONS = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.rating_file = open('rating.txt', mode='a')
        self.actual_user = None
        self.actual_user_score = 0
        self.game_options = None
        self.rating_file.close()

    def evaluate(self, hplay, cpuplay):
        if hplay == cpuplay:
            print("There is a draw ({})".format(cpuplay))
            self.actual_user_score += 50
        else:
            index_option = self.game_options.index(hplay)
            new_options = self.game_options[index_option + 1:] + self.game_options[:index_option]
            options_divider = len(new_options) // 2
            defeated_options = new_options[:options_divider]
            beating_options = new_options[options_divider:]
            if cpuplay in defeated_options:
                print("Sorry, but the computer chose {}".format(cpuplay))
            elif cpuplay in beating_options:
                print("Well done. The computer chose {} and failed!".format(cpuplay))
                self.actual_user_score += 100

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
            elif input_choice == '!rating':
                print(self.actual_user_score)
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
        self.actual_user = user_name

    def update_score(self):
        self.rating_file = open('rating.txt', mode='r')
        entries = self.rating_file.readlines()
        self.rating_file.close()
        for index, entry in enumerate(entries):
            if self.actual_user in entry:
                entries[index] = '{} {}\n'.format(self.actual_user, self.actual_user_score)

        self.rating_file = open('rating.txt', mode='w')
        self.rating_file.writelines(entries)

    def chose_options(self):
        options = input()
        self.game_options = options.split(',') if options else ['rock', 'paper', 'scissors']
        RPSEngine.OPTIONS = self.game_options

    def new_game(self):
        name = input('Enter your name: ')
        print('Hello, {}'.format(name))
        self.register_name(name)
        self.chose_options()
        print("Okay let's start")
        self.start_game()
        self.update_score()

    def human_play(self, choice):
        return choice if choice in RPSEngine.OPTIONS else None

    def cpu_play(self):
        choice = randint(0, 2)
        return RPSEngine.OPTIONS[choice]


if __name__ == '__main__':
    rps_game = RPSEngine()
    rps_game.new_game()
