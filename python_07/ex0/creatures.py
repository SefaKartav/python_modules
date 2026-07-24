import abc


class Creature(abc.ABC):
    def __init__(self, name: str, monster_type: str):
        self.name = name
        self.monster_type = monster_type

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> None:
        print(f"{self.name} is a {self.monster_type} type Creature")


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return ("Flameling uses Ember!")


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return ("Pyrodon uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return ("Aquabub uses Water Gun!")


class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return ("Torragon uses Hydro Pump!")
