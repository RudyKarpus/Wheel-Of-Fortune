from classes.game import Reward, Game
from classes.player import Player
from classes.word import Word
from classes.exceptions import NotAnPositiveNumberError, EmptyStringError
from model import Presenter
import pytest


def test_player_id():
    player = Player(1, "name")
    assert player.id == 1


def test_player_invalid_id():
    with pytest.raises(NotAnPositiveNumberError):
        Player(-1, "name")


def test_player_name():
    player = Player(1, "Bartek")
    assert player.name == "Bartek"


def test_player_basic_round_points_and_rewards():
    player = Player(1, "Bartek")
    assert player.rounds_points == 0
    assert player.rewards == []


def test_player_add_rounds_points():
    player = Player(1, "Bartek")
    assert player.rounds_points == 0
    player.add_rounds_points(100)
    assert player.rounds_points == 100


def test_player_invalid_points():
    player = Player(1, "Bartek")
    with pytest.raises(NotAnPositiveNumberError):
        player.add_rounds_points(-100)


def test_reward(monkeypatch):
    presenter = Presenter()

    def return_one(arg1, arg2):
        return 1
    monkeypatch.setattr('classes.game.randint', return_one)
    reward = Reward(presenter)
    assert reward.name == "wok"


def test_player_add_rounds_reward(monkeypatch):
    player = Player(1, "Bartek")
    presenter = Presenter()

    def return_two(arg1, arg2):
        return 2
    monkeypatch.setattr('classes.game.randint', return_two)
    reward = Reward(presenter)
    assert player.rounds_rewards == []
    player.add_rounds_reward(reward)
    assert player.rounds_rewards[0].name == "kosmetyki"


def test_player_add_points_and_rewards(monkeypatch):
    player = Player(1, "Bartek")
    presenter = Presenter()
    assert player.points == 0
    assert player.rewards == []
    player.add_rounds_points(100)

    def return_one(arg1, arg2):
        return 1
    monkeypatch.setattr('classes.game.randint', return_one)
    player.add_rounds_reward(Reward(presenter))
    player.add_rewards_and_points()
    assert player.points == 100
    assert player.rewards[0].name == "wok"


def test_player_rounds_account_reset():
    presenter = Presenter()
    player = Player(1, "Bartek")
    player.add_rounds_points(100)
    player.add_rounds_reward(Reward(presenter))
    assert player.rounds_points == 100
    assert player.rounds_rewards != []
    player.rounds_account_reset()
    assert player.rounds_points == 0
    assert player.rounds_rewards == []


def test_Word_word():
    word = Word("Koń", "Zwierze")
    assert "".join(word.word) == "Koń"


def test_Word_invalid_word():
    with pytest.raises(EmptyStringError):
        Word(category="Zwierze")


def test_Word_category():
    word = Word("Koń", "Zwierze")
    assert word.category == "Zwierze"


def test_Word_invalid_category():
    with pytest.raises(EmptyStringError):
        Word(word="Koń")


def test_Word_guessed_letters():
    word = Word("Koń i kot", "Zwierze")
    assert "".join(word.guessed_letters) == "*** * ***"


def test_Word_check_if_vowel():
    word = Word("Koń", "Zwierze")
    lits_of_vowels = list("aąeęiouóy")
    list_of_consonant = list("bcćdfghjklmnńprsśtwzżź")
    for vowel in lits_of_vowels:
        assert word.check_if_vowel(vowel) is True
    for consonant in list_of_consonant:
        assert word.check_if_vowel(consonant) is False


def test_Word_check_if_consonant():
    word = Word("Koń", "Zwierze")
    lits_of_vowels = list("aąeęiouóy")
    list_of_consonant = list("bcćdfghjklmnńprsśtwzżź")
    for vowel in lits_of_vowels:
        assert word.check_if_consonant(vowel) is False
    for consonant in list_of_consonant:
        assert word.check_if_consonant(consonant) is True


def test_Word_guess_later():
    player = Player(1, "Bartek")
    word = Word("Koń", "Zwierze")
    presenter = Presenter()
    presenter.game = Game(player)
    presenter.game.rounds_points = 200
    assert player.rounds_points == 0
    word.guess_letter("c", presenter)
    assert player.rounds_points == 0
    word.guess_letter("k", presenter)
    assert player.rounds_points == 200


def test_Word_check_if_guessed():
    player = Player(1, "Bartek")
    word = Word("Koń", "Zwierze")
    presenter = Presenter()
    presenter.game = Game(player)
    word.guess_letter("ń", presenter)
    assert word.check_if_guessed() is False
    word.guess_letter("o", presenter)
    assert word.check_if_guessed() is False
    word.guess_letter("k", presenter)
    assert word.check_if_guessed() is True
