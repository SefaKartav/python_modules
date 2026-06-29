import random


def gen_plagen_player_achievements():
    all_achievements = ["Crafting Genius", "World Savior",
                        "Untouchable", "Master Explorer",
                        "Collector Supreme", "Boss Slayer",
                        "Strategist", "Speed Runner",
                        "Survivor", "First Steps", "Sharp Mind",
                        "Unstoppable", "Treasure Hunter"]

    i = random.randint(3, 8)
    achievements = random.sample(all_achievements, k=i)
    return set(achievements)


def main():
    print("=== Achievement Tracker System ===\n")
    Alice = gen_plagen_player_achievements()
    Bob = gen_plagen_player_achievements()
    Charlie = gen_plagen_player_achievements()
    Dylan = gen_plagen_player_achievements()
    All = Alice.union(Bob, Charlie, Dylan)
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}\n")

    print(f"All distinct achievements: {Alice.union(Bob, Charlie, Dylan)}\n")
    print(f"Common achievements: {Alice.intersection(Bob, Charlie, Dylan)}\n")
    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Bob, Alice, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Bob, Charlie, Alice)}\n")
    notAlice = All.difference(Alice)
    notBob = All.difference(Bob)
    notCharlie = All.difference(Charlie)
    notDylan = All.difference(Dylan)

    print(f"Alice is missing: {notAlice}")
    print(f"Bob is missing: {notBob}")
    print(f"Charlie is missing: {notCharlie}")
    print(f"Dylan is missing: {notDylan}")


if __name__ == "__main__":
    main()
