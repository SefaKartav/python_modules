from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test(factory: CreatureFactory):
    print("Testing factory")
    base_creature = factory.create_base()
    base_creature.describe()
    print(base_creature.attack())
    evolved_creature = factory.create_evolved()
    evolved_creature.describe()
    print(evolved_creature.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory):
    monster1 = factory1.create_base()
    monster2 = factory2.create_base()

    monster1.describe()
    print("vs.")
    monster2.describe()
    print("fight!")
    print(monster1.attack())
    print(monster2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test(flame_factory)
    print("\n")
    test(aqua_factory)
    print("\n")
    print("Testing battle")
    test_battle(flame_factory, aqua_factory)
