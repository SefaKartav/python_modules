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
        action = random.choice(actions)
        gen: tuple[str, str] = (player, action)

        yield gen


def wiper(event_list: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    random_index = random.randint(0, len(event_list) - 1)
    item = event_list.pop(random_index)
    yield item

def main():
    print("=== Game Data Stream Processor ===")

    fallow = forever_event()

    for i in range(1000):
        event = next(fallow)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")


if __name__ == "__main__":
    main()
