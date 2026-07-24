from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability

class Sproutling(Creature, HealCapability):
    def __init__(self):
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."


class Bloomelle(Sproutling):
    def __init__(self):
        Sproutling(self, "Bloomelle", "Grassy/Fairy")
