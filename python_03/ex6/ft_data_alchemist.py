import random


def events():
    try_list = ["alice", "bob", "Charlie", "dylan", "Emma",
                "Gregory", "john", "kevin", "Liam", "sefa"]

    first_list = [name.capitalize() for name in try_list]
    second_list = [name for name in try_list if name[0].istitle()]
    list_score = {name: random.randint(0, 1000) for name in second_list}
    score_average = sum(list_score.values()) / len(list_score)
    is_average = {
        name: score
        for name, score in list_score.items()
        if score > score_average
    }

    print(f"Initial list of players: {try_list}")
    print(f"New list with all names capitalized: {first_list}")
    print(f"New list of capitalized names only: {second_list}")
    print(f"Score dict: {list_score}")
    print(f"Score average is {score_average}")
    print(f"High scores: {is_average}")


if __name__ == "__main__":
    events()
