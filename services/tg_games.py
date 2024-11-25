from typing import List


class Game:
    def __init__(self, visual_name: str, official_name: str, url: str):
        self.__visual_name = visual_name
        self.__official_name = official_name
        self.__url = 'https://prizes.gamee.com/game-bot/' + url

    @property
    def visual_name(self):
        return self.__visual_name

    @property
    def official_name(self):
        return self.__official_name

    @property
    def url(self):
        return self.__url

    def __str__(self):
        return self.__official_name


class GameList:
    def __init__(self):
        self.__GAME_OBJECTS = []

    @property
    def list(self) -> List:
        return self.__GAME_OBJECTS

    def add(self, *args: 'Game'):
        for game in args:
            self.__GAME_OBJECTS.append(game)

    def get_list_short_names(self):
        return [game.official_name for game in self.__GAME_OBJECTS]

    def __len__(self):
        return len(self.__GAME_OBJECTS)


karatekido2 = Game('Karate Kido 2', 'karatekido2', '9lEE0Oh-e6c930553f006bfa3f60677881fc1b7c9bbcbf7b')
basketboyrush = Game('Basket Boy Rush', 'basketboyrush', 'qxpwxJTh7-6914d5310dfd4c23b76408266a400f3c49836258')
spikyfish3 = Game('Spiky Fish 3', 'spikyfish3', 'zcvFFeQ0t-d834b40d328def0af84c046af92af02a7115bad1')
basketboy = Game('Basket Boy', 'basketboy', 'DwVcZZnbP-1d57998dc54d033c6865861a10e08037bdeb2762')
gravityninjaemeraldcity = Game('Gravity Ninja: Emerald City', 'gravityninjaemeraldcity',
                               'ZTaHq2lM-5414dee415867b85dffa0390ff968a6c95ca9558')
keepitup = Game('Keep it UP', 'keepitup', 'a3pyHGoadz-ef79e60ef0edd67bb9b0f7a09be90d160a80836a')

games = GameList()
games.add(karatekido2, basketboyrush, spikyfish3, basketboy, gravityninjaemeraldcity, keepitup)
