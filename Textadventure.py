import time
import sys


class Entity:
    def __init__(self):
        # hp = 100
        # armor = 1
        pass


class Player(Entity):

    def __init__(self, startpos=0):
        Entity.__init__(self)
        # inventory = []
        self.position = startpos

    def move(self, direction):
        self.position = self.position + direction


class Room:

    def __init__(self, start_position):
        self.position = start_position
        self.decisions = {"warten": self.describe_room,
                           "vorwärts": self.go_north,
                           "zurück": self.go_south,
                           "hilfe": self.show_help,
                           "aufgeben": self.end_game
                           }
        self.ls_str_desc = [
            "Du siehst einen leeren Korridor, der durch eine Fackel an der Wand beleuchtet wird",
            "Du verlässt den Korridor nach Norden",
            "Du verlässt den Korridor nach Süden",
            ""
        ]

    def end_game(self):
        input("Das Spiel ist beendet. Drücke eine beliebige Taste zum Beenden")
        exit()

    def show_help(self):
        for i in self.decisions.keys():
            print(i)

    def describe_room(self):
        print(self.ls_str_desc[0])

    def go_north(self):
        player.move(1)
        print(self.ls_str_desc[1])

    def go_south(self):
        player.move(-1)
        print(self.ls_str_desc[2])

    def look_around(self):
        print(self.ls_str_desc[3])

    def decision(self):
        print("Was möchtest du tun?")
        print_options()
        actual_world.map[player.position].decisions[input()]()


class World:
    map = []


def print_options():
    for i in actual_world.map[player.position].decisions.keys():
        print(i)


def create_world(world: World):
    world.map.append(Room(0))
    world.map.append(Room(1))
    world.map.append(Room(2))

    #world.map[0].decisions = {}

    world.map[0].ls_str_desc[0] = """Der Korridor wird gesäumt von Skeletten, die an die Wand gekettet sind. 
    Sie hängen an Armen und Beinen gefesselt von den Wänden."""
    world.map[1].ls_str_desc[0] = """Der Korridor endet hier. Vor dir siehst du die Rückseite einer Geheimtür.
    Sie ist nur leicht angelehnt"""
    world.map[2].ls_str_desc[0] = """Du stehst in einem Thronraum. Ein Kampf zwischen einem großen schwarzen Ritter mit
    einer blutroten Krone und einer Gruppe Abenteurern, die dich verblüfft ansehen, nachdem du hinter dem Thron 
    hervor trittst."""


if __name__ == "__main__":

    actual_world = World()
    create_world(actual_world)
    player = Player()
    player.position = 0
    print("\nWillkommen zum Marfeyows Textabenteuer. \n Du wachst in einem Tunnel auf. ")
    while player.position <= len(actual_world.map):
        actual_world.map[player.position].describe_room()
        actual_world.map[player.position].decision()

    print("--- under construction ---")
