from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QTimer, QTime
from PySide2.QtGui import QPixmap
from ui.ui_entrancewindow import Ui_Form as entrancescreen
from ui.ui_loginwindow import Ui_Form as loginscreen
from ui.ui_roundwindow import Ui_Form as roundscreen
from ui.ui_finalround import Ui_Form as finalroundscreen
from ui.ui_finalwindow import Ui_Form as finalscreen
from classes.player import Player
from classes.game import Game
from model import ButtonHolder
from classes.constants import WheelPrizes, Letters, UiLabelsTexts
from random import randint
import math


class EntranceScreen(QWidget):
    def __init__(self, presenter, parent=None):
        super().__init__(parent)
        self.ui = entrancescreen()
        self.ui.setupUi(self)
        self.presenter = presenter
        self.ui.startButton.clicked.connect(self.go_to_loginscreen)

    def go_to_loginscreen(self):
        self.presenter.mainwindow.next_layout()


class LogInScreen(QWidget):
    def __init__(self, presenter, parent=None):
        super().__init__(parent)
        self.times_button_clicked = 0
        self.presenter = presenter
        self.ui = loginscreen()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.addButtonAction)

    def addButtonAction(self):
        self.times_button_clicked += 1
        self.presenter.add_player(Player(
            self.times_button_clicked,
            self.ui.addPlayerTextEdit.toPlainText()))
        self.ui.addPlayerTextEdit.setPlainText("...")
        self.ui.label.setText(
            f"Wprowadź imię gracza nr. {self.times_button_clicked+1}")
        self.ui.label.update()
        if self.times_button_clicked == 3:
            self.presenter.screensHolder.round_screen.setupScreenData()
            self.presenter.mainwindow.next_layout()


class RoundScreen(QWidget):
    def __init__(self, presenter, parent=None):
        super().__init__(parent)
        presenter.screensHolder.round_screen = self
        self.presenter = presenter
        self.ui = roundscreen()
        self.ui.setupUi(self)
        self.ui.dial.setEnabled(False)

    def setupScreenData(self):
        self.ui.label_name1.setText(self.presenter.playerlist[0].name)
        self.ui.label_name2.setText(self.presenter.playerlist[1].name)
        self.ui.label_name3.setText(self.presenter.playerlist[2].name)
        self.presenter.button_holder = ButtonHolder(
            self.ui.ConsonantButton, self.ui.answerButton,
            self.ui.vowelButton, self.ui.roll_the_wheel_button)
        self.presenter.game = Game(self.presenter.playerlist[0])
        self.presenter.game.draw_word(self.presenter.wordlist)
        pixmap = QPixmap()
        if pixmap.load("wheeloffortune.png"):
            self.ui.label_wheel.setPixmap(pixmap)
        self.ui.dial.setSliderPosition(10)
        self.ui.roll_the_wheel_button.clicked.connect(self.speen_the_wheel)
        self.ui.answerButton.clicked.connect(self.button_answer_action)
        self.ui.vowelButton.clicked.connect(self.button_vowel_acton)
        self.ui.ConsonantButton.clicked.connect(self.button_consonant_action)
        self.updateScreenData()

    def updateScreenData(self):
        self.ui.label_round_number.setText(
            UiLabelsTexts.round.value + str(self.presenter.game.round_number))
        if self.presenter.game.word.check_if_guessed():
            self.next_round()
        self.ui.label_points1.setText(str(
            self.presenter.playerlist[0].rounds_points))
        self.ui.label_points2.setText(str(
            self.presenter.playerlist[1].rounds_points))
        self.ui.label_points3.setText(str(
            self.presenter.playerlist[2].rounds_points))
        if self.presenter.button_holder.wheel_acces is False:
            self.presenter.button_holder.answer_acces = False
        if (self.presenter.game.players_moves > 0 and
                self.presenter.button_holder.wheel_acces is True and
                self.presenter.game.active_player.rounds_points >= 200):
            self.presenter.button_holder.vow_acces = True
        self.change_button_color(self.presenter.button_holder.button_con,
                                 self.presenter.button_holder.con_acces)
        self.change_button_color(self.presenter.button_holder.button_answer,
                                 self.presenter.button_holder.answer_acces)
        self.change_button_color(self.presenter.button_holder.button_vow,
                                 self.presenter.button_holder.vow_acces)
        self.change_button_color(self.presenter.button_holder.button_wheel,
                                 self.presenter.button_holder.wheel_acces)
        if self.presenter.game.active_player.id == 1:
            self.ui.radioButton_player1.setChecked(True)
        elif self.presenter.game.active_player.id == 2:
            self.ui.radioButton_player2.setChecked(True)
        elif self.presenter.game.active_player.id == 3:
            self.ui.radioButton_player3.setChecked(True)
        self.ui.label_category.setText(
            UiLabelsTexts.category.value +
            "".join(self.presenter.game.word.category))
        self.ui.label_word.setText(
            "".join(self.presenter.game.word.guessed_letters))
        self.ui.answerTextEdit.setPlainText("")

    def change_button_color(self, button, is_button_accesible):
        if is_button_accesible:
            button.setEnabled(True)
            button.setStyleSheet("""
            QPushButton {background:rgb(0,128,0); color: black;}
            """)
        else:
            button.setEnabled(False)
            button.setStyleSheet("""
            QPushButton {background:rgb(255,0,0); color: black;}
            """)

    def speen_the_wheel(self):
        roll = randint(0, 240)
        self.ui.dial.setSliderPosition(roll)
        reward = WheelPrizes.prices_list.value[math.floor(roll/10)-1]
        reward.initialize(self.presenter)
        self.ui.label_wheel_worth.setText(str(reward))
        self.updateScreenData()

    def button_consonant_action(self):
        letter = self.ui.answerTextEdit.toPlainText()
        game = self.presenter.game
        if len(letter) == 1 and game.word.check_if_consonant(letter):
            if game.word.guess_letter(letter, self.presenter):
                game.players_moves += 1
            else:
                game.next_player(self.presenter.playerlist)
        else:
            game.next_player(self.presenter.playerlist)
        self.presenter.button_holder.spin_wheel_state()
        self.updateScreenData()

    def button_answer_action(self):
        answer = self.ui.answerTextEdit.toPlainText()
        game = self.presenter.game
        if answer.lower() == "".join(game.word.word).lower():
            self.next_round()
        else:
            self.presenter.button_holder.spin_wheel_state()
            game.next_player(self.presenter.playerlist)
        self.updateScreenData()

    def button_vowel_acton(self):
        letter = self.ui.answerTextEdit.toPlainText()
        game = self.presenter.game
        if len(letter) == 1 and game.word.check_if_vowel(letter):
            if game.word.buy_letter(letter, game.active_player):
                game.players_moves += 1
            else:
                game.next_player(self.presenter.playerlist)
        else:
            game.next_player(self.presenter.playerlist)
        self.presenter.button_holder.spin_wheel_state()
        self.updateScreenData()

    def next_round(self):
        self.presenter.game.active_player.add_rewards_and_points()
        if self.presenter.game.round_number == 3:
            self.presenter.screensHolder.final_round_screen.setUpFinalRound()
            self.presenter.mainwindow.next_layout()
        else:
            for player in self.presenter.playerlist:
                player.rounds_account_reset()
            self.presenter.game.round_number += 1
            self.presenter.game.draw_word(self.presenter.wordlist)
            self.presenter.button_holder.spin_wheel_state()
            self.updateScreenData()


class FinalRoundScreen(QWidget):
    def __init__(self, presenter, parent=None):
        super().__init__(parent)
        self.presenter = presenter
        presenter.screensHolder.final_round_screen = self
        self.ui = finalroundscreen()
        self.ui.setupUi(self)
        self.ui.answerButton.clicked.connect(self.answer_button_action)
        self.numbers_button_clicked = 0

    def setUpFinalRound(self):
        self.decideFinalist()
        self.ui.label_instruction.setText(
                UiLabelsTexts.final_round_description.value.format(
                    self.draw_letters()))
        self.setUpWord()
        self.ui.label_category.setText("Kategoria: "+"".join(
            self.presenter.game.word.category))
        self.ui.label_2.setText("".join(
            self.presenter.game.word.guessed_letters))

    def draw_letters(self):
        letters = Letters.all_leters.value[
                randint(0, len(Letters.all_leters.value)-1)]
        while len(letters) <= 11:
            letter = Letters.all_leters.value[
                randint(0, len(Letters.all_leters.value)-1)]
            if letter not in letters:
                letters = letters + ", "+letter
        self.drawn_letters = letters
        return letters

    def answer_button_action(self):
        if self.numbers_button_clicked == 0:
            numbers_of_letters = 0
            for letter in self.ui.answerTextEdit.toPlainText():
                if self.presenter.game.word.check_if_letter(letter):
                    numbers_of_letters += 1
            if numbers_of_letters == 4:
                self.numbers_button_clicked += 1
                for letter in Letters.all_leters.value:
                    if letter in self.ui.answerTextEdit.toPlainText():
                        self.presenter.game.word.guess_letter(
                            letter, self.presenter)
            self.ui.answerTextEdit.setPlainText("")
            self.ui.label_instruction.setHidden(True)
            self.ui.label_2.setText("".join(
                self.presenter.game.word.guessed_letters))
            self.timer = QTimer()
            self.time = QTime(0, 0, 5)
            self.timer.timeout.connect(self.timerCountDown)
            self.timer.start(1000)
            self.number_of_ticks = 0
        elif self.numbers_button_clicked == 1:
            self.numbers_button_clicked += 1
            self.timer.stop()
            if (self.ui.answerTextEdit.toPlainText().lower() ==
                    "".join(self.presenter.game.word.word).lower()):
                self.player_win()
            else:
                self.player_lose()

    def setUpWord(self):
        self.presenter.game.draw_word(self.presenter.wordlist)
        for letter in self.drawn_letters:
            if letter in Letters.all_leters.value:
                self.presenter.game.word.guess_letter(letter, self.presenter)

    def player_win(self):
        self.ui.label.setText(UiLabelsTexts.final_round_win.value)
        self.ui.answerButton.setText(UiLabelsTexts.final_round_continue.value)
        self.presenter.game.active_player.rewards.append("Polonez")
        self.presenter.screensHolder.final_screen.setUpData()
        self.ui.answerButton.clicked.connect(
            self.presenter.mainwindow.next_layout)

    def player_lose(self):
        self.ui.label.setText(UiLabelsTexts.final_round_lose.value)
        self.ui.answerButton.setText(UiLabelsTexts.final_round_continue.value)
        self.presenter.screensHolder.final_screen.setUpData()
        self.ui.answerButton.clicked.connect(
            self.presenter.mainwindow.next_layout)

    def timerCountDown(self):
        self.number_of_ticks += 1
        if self.number_of_ticks == 6:
            self.timer.stop()
            self.player_lose()
        else:
            self.time = self.time.addSecs(-1)
            self.ui.timeEdit.setTime(self.time)

    def decideFinalist(self):
        players = self.presenter.playerlist
        if players[0].points >= players[1].points:
            if players[0].points >= players[2].points:
                self.presenter.game.active_player = players[0]
            else:
                self.presenter.game.active_player = players[2]
        else:
            if players[1].points >= players[2].points:
                self.presenter.game.active_player = players[1]
            else:
                self.presenter.game.active_player = players[2]


class FinalScreen(QWidget):
    def __init__(self, presenter, parent=None):
        super().__init__(parent)
        self.presenter = presenter
        presenter.screensHolder.final_screen = self
        self.ui = finalscreen()
        self.ui.setupUi(self)

    def setUpData(self):
        self.ui.label_player_name_1.setText(self.presenter.playerlist[0].name)
        self.ui.label_player_points_1.setText(
            str(self.presenter.playerlist[0].points))
        text = ""
        for reward in self.presenter.playerlist[0].rewards:
            text = text + str(reward) + "\n"
        self.ui.label_player_rewards_1.setText(text)
        self.ui.label_player_name_2.setText(self.presenter.playerlist[1].name)
        self.ui.label_player_points_2.setText(
            str(self.presenter.playerlist[1].points))
        text = ""
        for reward in self.presenter.playerlist[1].rewards:
            text = text + str(reward) + "\n"
        self.ui.label_player_rewards_2.setText(text)
        self.ui.label_player_name_3.setText(self.presenter.playerlist[2].name)
        self.ui.label_player_points_3.setText(
            str(self.presenter.playerlist[2].points))
        text = ""
        for reward in self.presenter.playerlist[2].rewards:
            text = text + str(reward) + "\n"
        self.ui.label_player_rewards_3.setText(text)
