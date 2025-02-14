import json
from classes.word import Word
from classes.constants import FilePaths


class Presenter():
    def __init__(self, mainwindow=None, layoutstackholder=0):
        self.screensHolder = ScreensHolder()
        self._mainwindow = mainwindow
        self._layoutstackholder = layoutstackholder
        self.playerlist = []
        self.wordlist = self.setupWordList()
        self._game = None
        self._button_holder = None
        self.rewardslist = self.setupRewardsList()

    @property
    def mainwindow(self):
        return self._mainwindow

    @mainwindow.setter
    def mainwindow(self, window):
        self._mainwindow = window

    @property
    def layoutstackholder(self):
        return self._layoutstackholder

    @layoutstackholder.setter
    def layoutstackholder(self, layoutstackholder):
        self._layoutstackholder = layoutstackholder

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        self._game = game

    @property
    def button_holder(self):
        return self._button_holder

    @button_holder.setter
    def button_holder(self, new_button_holder):
        self._button_holder = new_button_holder

    def nextlayout(self):
        self.layoutstackholder = self.layoutstackholder + 1

    def add_player(self, new_player):
        self.playerlist.append(new_player)

    def setupWordList(self):
        list_of_word = []
        with open(FilePaths.games_words_list.value, "r",
                  encoding='utf-8') as file:
            data = json.load(file)
        for word in data["words"]:
            list_of_word.append(Word(word["word"], word["category"]))
        return list_of_word

    def setupRewardsList(self):
        list_of_rewards = []
        with open(FilePaths.games_rewards_list.value, "r",
                  encoding='utf-8') as file:
            for line in file:
                list_of_rewards.append(line.strip())
        return list_of_rewards


class ButtonHolder():
    def __init__(self, buttoncon, buttonasnwer, buttonvow, buttonwheel):
        self._button_con = buttoncon
        self.con_acces = False
        self._button_answer = buttonasnwer
        self.answer_acces = False
        self._button_vow = buttonvow
        self.vow_acces = False
        self._button_wheel = buttonwheel
        self.wheel_acces = True

    @property
    def button_con(self):
        return self._button_con

    @property
    def button_answer(self):
        return self._button_answer

    @property
    def button_vow(self):
        return self._button_vow

    @property
    def button_wheel(self):
        return self._button_wheel

    def answer_state(self):
        self.vow_acces = False
        self.wheel_acces = False
        self.answer_acces = True
        self.con_acces = True

    def spin_wheel_state(self):
        self.vow_acces = False
        self.wheel_acces = True
        self.answer_acces = True
        self.con_acces = False


class ScreensHolder():
    def __init__(self):
        self._round_screen = None
        self._final_round_screen = None
        self._final_screen = None

    @property
    def round_screen(self):
        return self._round_screen

    @round_screen.setter
    def round_screen(self, screen):
        self._round_screen = screen

    @property
    def final_round_screen(self):
        return self._final_round_screen

    @final_round_screen.setter
    def final_round_screen(self, screen):
        self._final_round_screen = screen

    @property
    def final_screen(self):
        return self._final_screen

    @final_screen.setter
    def final_screen(self, screen):
        self._final_screen = screen
