from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count+= 1
        return count
    return counter

def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power
    def spell(add_power: int) -> int:
        nonlocal power
        power += add_power
        return power
    return spell

def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type}, {item_name}"
    return enchantment

def memory_vault() -> dict[str, Callable]:
    pass


if __name__ == "__main__":
    print("Testing mage")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"Counter a: ", counter_a())
    print(f"Counter a: ", counter_a())
    print(f"Counter b: ", counter_b())

    print("\nTesting spell")
    spell1 = spell_accumulator(100)
    print("try1: ", spell1(14))

    print("\nTesting enchantment")
    spell1 = enchantment_factory("sword")
    trying = spell1("Sefa")
    print("try1: ", trying)



