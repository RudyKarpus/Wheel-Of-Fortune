from .exceptions import NotAnPositiveNumberError


class Player():
    def __init__(self, id, name):
        if id > 0:
            self._id = id
        else:
            raise NotAnPositiveNumberError
        self._name = name
        self._rounds_points = 0
        self._points = 0
        self._rounds_rewards = []
        self._rewards = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def id(self):
        return self._id

    @property
    def rounds_points(self):
        return self._rounds_points

    @rounds_points.setter
    def rounds_points(self, new_points):
        self._rounds_points = new_points

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, new_points):
        self._points = new_points

    @property
    def rounds_rewards(self):
        return self._rounds_rewards

    @rounds_rewards.setter
    def rounds_rewards(self, new_rewards):
        self._rounds_rewards = new_rewards

    @property
    def rewards(self):
        return self._rewards

    @rewards.setter
    def rewards(self, new_rewards):
        self._rewards = new_rewards

    def add_rounds_points(self, new_points):
        if new_points >= 0:
            self.rounds_points = self.rounds_points + new_points
        else:
            raise NotAnPositiveNumberError

    def add_rounds_reward(self, new_reward):
        self.rounds_rewards.append(new_reward)

    def add_rewards_and_points(self):
        for reward in self.rounds_rewards:
            self.rewards.append(reward)
        self.rounds_rewards = []
        self.points = self.points + self.rounds_points
        self.rounds_points = 0

    def rounds_account_reset(self):
        self.rounds_rewards = []
        self.rounds_points = 0

    def __lt__(self, other_player):
        return self.points > other_player.points
