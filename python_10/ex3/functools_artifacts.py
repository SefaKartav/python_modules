import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operation_list: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operation_list:
        raise ValueError(f"Unknown operation: {operation}")
    selected = operation_list[operation]
    return functools.reduce(selected, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, 50, "Fire")
    ice = functools.partial(base_enchantment, 50, "Ice")
    earth = functools.partial(base_enchantment, 50, "Earth")

    return {
        "fire": fire,
        "ice": ice,
        "earth": earth
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def base_spell(arg: Any) -> str:
        return "Unkown spell type"

    @base_spell.register
    def int_spell(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @base_spell.register
    def str_spell(arg: str) -> str:
        return f"Enchantment: {arg}"

    @base_spell.register
    def list_spell(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return base_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    try_list = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(try_list, 'add')}")
    print(f"Product: {spell_reducer([20, 30, 40, 10], 'multiply')}")
    print(f"Max: {spell_reducer(try_list, 'max')}")
    print(f"Min: {spell_reducer(try_list, 'min')}")

    print("\nTesting partial enchanter...")

    def base_try(power: int, element: str, target: str) -> str:
        return f"Casting {element} magic with {power} power on {target}"

    trying = partial_enchanter(base_try)
    fire = trying["fire"]
    print(fire("Goblin"))
    print(trying["ice"]("Dragon"))

    print("\nTesting memoized fibonacci...")

    print(f"Fibonacci(10): {memoized_fibonacci(10)}")
    print(f"Fibonacci(5): {memoized_fibonacci(5)}")
    print(f"Fibonacci(3): {memoized_fibonacci(3)}")

    print("\nTesting spell dispatcher...")
    trying_spell = spell_dispatcher()
    print(f"Trying int: {trying_spell(42)}")
    print(f"Trying str: {trying_spell("Sefa")}")
    print(f"Trying list: {trying_spell([12, 15, 19])}")
    print(f"Trying unknow: {trying_spell(14.9)}")
