from random import randint


class Game():
    def __init__(self, player):
        self.word = None
        self.active_player = player
        self.rounds_points = None
        self.rounds_reward = None
        self.players_moves = 0
        self.round_number = 1

    def next_player(self, playerlist):
        self.active_player = playerlist[self.active_player.id % 3]
        self.players_moves = 0

    def draw_word(self, wordlist):
        self.word = wordlist[randint(0, len(wordlist)-1)]
        self.players_moves = 0


class Reward():
    def __init__(self, presenter):
        self.name = self.draw_reward(presenter)

    def draw_reward(self, presenter):
        return presenter.rewardslist[
            randint(0, len(presenter.rewardslist)-1)]

    def __str__(self):
        return self.name
