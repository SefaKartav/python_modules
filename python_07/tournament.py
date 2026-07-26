from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (
    BattleStrategy, NormalStrategy, AggrassiveStrategy,
    DefensiveStrategy, InvalidStrategyError
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    length = len(opponents)
    for i in range(length):
        for j in range(i + 1, length):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print("* Battle *")
            c1.describe()
            print("vs.")
            c2.describe()
            print("now fight!")

            try:
                strategy1.act(c1)
                strategy2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggrassiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggrassiveStrategy())
    ])
