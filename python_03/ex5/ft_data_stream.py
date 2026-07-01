import random
import typing
from typing import Generator

def forever_event() -> Generator[tuple[str, str], None, None]:
    players = ["Sefa", "Merve", "Nurettin", "Dondu", "Hakan",
               "Enes", "Metehan", "Eda", "Feyza", "Rabia", "Zeynep",
               "Emre", "Eren"]
    actions = ["eat", "run", "sleep", "grap", "move", "climb", "swim",
               "work", "walk", "love", "drink"]

    while True:
        player = random.choice(players)
        action = random.choice(action)
        gen: tuple[str, str] = (player, action)

        yield gen


def wiper(event_list: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    random_index = random.randint(0, len(event_list) - 1)
    item = event_list.pop(random_index)

def main():
    print("=== Game Data Stream Processor ===")

    for i in 1000:
