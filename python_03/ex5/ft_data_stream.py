import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
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


def consume_event(
        event_list: list[tuple[str, str]],
        ) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        random_index = random.randint(0, len(event_list) - 1)
        item = event_list.pop(random_index)
        yield item


def main():
    print("=== Game Data Stream Processor ===")

    fallow = gen_event()

    for i in range(1000):
        event = next(fallow)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_event_list = []
    for x in range(10):
        ten_event_list.append(next(fallow))

    print(f"Built list of 10 events: {ten_event_list}")

    for y in consume_event(ten_event_list):
        print(f"Got event from list: {y}")
        print(f"Remains in list: {ten_event_list}")


if __name__ == "__main__":
    main()
