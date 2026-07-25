from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal(healingcreature: HealingCreatureFactory):
    print("base:")
    base_creature = healingcreature.create_base()
    base_creature.describe()
    print(base_creature.attack())
    print(base_creature.heal())

    print("evolved:")
    evolved_creature = healingcreature.create_evolved()
    evolved_creature.describe()
    print(evolved_creature.attack())
    print(evolved_creature.heal())


def test_trans(transcreature: HealingCreatureFactory):
    print("base:")
    base_creature = transcreature.create_base()
    base_creature.describe()
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())

    print("evolved:")
    evolved_creature = transcreature.create_evolved()
    evolved_creature.describe()
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    Healingmonsterbase = HealingCreatureFactory()
    test_heal(Healingmonsterbase)
    print("\nTesting Creature with transform capability")
    Healingmonsterevolved = TransformCreatureFactory()
    test_trans(Healingmonsterevolved)
