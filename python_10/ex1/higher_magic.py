from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def mega(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return mega


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence_spell


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} power"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} power"

    def is_strong_enough(target: str, power: int) -> bool:
        return power >= 20

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res = combined("Dragon", 10)
    print(f"Combined spell result: {res[0]}, {res[1]}")

    print("\nTesting power amplifier...")
    combined1 = power_amplifier(fireball, 3)
    res1 = combined1("Dragon", 10)
    print(res1)

    print("\nTesting conditional caster - True")
    combined2 = conditional_caster(is_strong_enough, heal)
    res2 = combined2("Dragon", 30)
    print(res2)

    print("\nTesting conditional caster - False")
    combined3 = conditional_caster(is_strong_enough, heal)
    res3 = combined3("Dragon", 10)
    print(res3)

    print("\nTesting spell sequence")
    combined4 = spell_sequence([fireball, heal, fireball])
    res4 = combined4("Dragon", 15)
    print(res4)
