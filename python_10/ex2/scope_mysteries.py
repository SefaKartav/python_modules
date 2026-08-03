from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
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
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")
    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    spell1 = spell_accumulator(100)
    print(f"Base 100, add 20: {spell1(20)}")
    print(f"Base 100, add 30: {spell1(30)}")

    print("\nTesting enchantment factory...")
    flame_enchanter = enchantment_factory("Flaming")
    ice_enchanter = enchantment_factory("Frozen")
    print(flame_enchanter("Sword"))
    print(ice_enchanter("Shield"))

    print("\nTesting memory vault...")
    mem = memory_vault()
    mem['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret' : {mem['recall']('secret')}")
    print(f"Recall 'unknown' : {mem['recall']('unknown')}")
