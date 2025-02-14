from .exceptions import EmptyStringError
from .constants import Letters


class Word():
    def __init__(self, word="", category=""):
        if len(word) != 0:
            self._word = list(word)
        else:
            raise EmptyStringError
        if len(category) != 0:
            self._category = category
        else:
            raise EmptyStringError

        self._guessed_letters = ['*' if letter != ' ' else ' '
                                 for letter in word]

    @property
    def word(self):
        return self._word

    @property
    def category(self):
        return self._category

    @property
    def guessed_letters(self):
        return self._guessed_letters

    def guess_letter(self, letter, presenter):
        game = presenter.game
        if ((letter in self.word or letter.upper() in self.word) and
                letter not in self.guessed_letters):
            occurences = 0
            for word_letter in range(0, len(self.word)):
                if letter == self.word[word_letter].lower():
                    occurences += 1
                    self.guessed_letters[word_letter] = self.word[word_letter]
            if presenter.game.rounds_points is not None:
                game.active_player.add_rounds_points(game.rounds_points *
                                                     occurences)
            else:
                game.active_player.add_rounds_reward(game.rounds_reward)
            return True
        else:
            return False

    def buy_letter(self, letter, player):
        player.rounds_points = player.rounds_points - 200
        if letter in self.word and letter not in self.guessed_letters:
            for word_letter in range(0, len(self.word)):
                if letter == self.word[word_letter].lower():
                    self.guessed_letters[word_letter] = self.word[word_letter]
            return True
        else:
            return False

    def check_if_guessed(self):
        if self.guessed_letters == self.word:
            return True
        else:
            return False

    def check_if_vowel(self, letter):
        return letter in Letters.vowels.value

    def check_if_consonant(self, letter):
        return letter in Letters.consonants.value

    def check_if_letter(self, letter):
        return len(letter) == 1
