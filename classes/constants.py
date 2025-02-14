from enum import Enum
from .wheelstates import Points, Stop, Bankrupt, RandomReward


class Letters(Enum):
    all_leters = "aąeęiouóybcćdfghjklłmnńprsśtwzżź"
    vowels = "aąeęiouóy"
    consonants = "bcćdfghjklmnńprsśtwzżź"


class WheelPrizes(Enum):
    prices_list = [
                    Points(3000), RandomReward(), Points(150), Points(250),
                    Points(300), RandomReward(), Points(200), Bankrupt(),
                    Points(2000), Points(350), Points(250), Points(500),
                    RandomReward(), Points(200), Points(1500), Points(250),
                    Points(500), Bankrupt(), Points(400), Points(1500),
                    Points(250), Stop(), Points(400), Points(200)]


class FilePaths(Enum):
    games_words_list = "files/words.json"
    games_rewards_list = "files/rewards.txt"


class UiLabelsTexts(Enum):
    round = "Runda "
    category = "Kategoria: \n"
    final_round_description = ("Zostały ci już wylosowane 5 liter: {:}.\n" +
                               "Podaj teraz 4 następne litery, które " +
                               "które chcesz odkryć.\nNastępnie będziesz" +
                               " miał 5 sekund na zgadnięcie hasła.")
    final_round_win = "Gratulacje udało ci się wygrać Poloneza!!!"
    final_round_lose = "Niestety nie udało ci się wygrać Poloneza :("
    final_round_continue = "Kontynuj"
