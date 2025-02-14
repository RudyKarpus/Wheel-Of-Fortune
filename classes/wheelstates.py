from .game import Reward


class Stop():
    def initialize(self, presenter):
        presenter.button_holder.spin_wheel_state()
        presenter.game.next_player(presenter.playerlist)

    def __str__(self):
        return "Stop"


class Bankrupt():
    def initialize(self, presenter):
        presenter.button_holder.spin_wheel_state()
        presenter.game.active_player.rounds_account_reset()
        presenter.game.next_player(presenter.playerlist)

    def __str__(self):
        return "Bankrut"


class Points():
    def __init__(self, points):
        self.points = points

    def initialize(self, presenter):
        presenter.button_holder.answer_state()
        presenter.game.rounds_points = self.points
        presenter.game.rounds_reward = None

    def __str__(self):
        return str(self.points)


class RandomReward():
    def initialize(self, presenter):
        self.reward = Reward(presenter)
        presenter.game.rounds_points = None
        presenter.game.rounds_reward = self.reward
        presenter.button_holder.answer_state()

    def __str__(self):
        return str(self.reward.name)
