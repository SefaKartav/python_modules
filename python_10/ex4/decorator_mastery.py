import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None:
                for arg in reversed(args):
                    if isinstance(arg, int):
                        power = arg
                        break

            if power is None or power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, "
                              f"retrying... (attempt "
                              f"{attempt}/{max_attempts})")
                    else:
                        return (f"Spell casting failed "
                                f"after {max_attempts} attempts")
            return None
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("===============================================")
    print("Testing spell timer...")
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Result: Fireball cast!"

    print(fireball())

    print("===============================================")
    print("\nTesting power validator...")
    @power_validator(min_power=20)
    def flexible_spell(*args: Any, **kwargs: Any) -> str:
        return "BOOM, successfully"

    print(f"Test 1: ", flexible_spell("Target1", power=50))
    print(f"Test 2: ", flexible_spell("Target2", 30, "ExtraArg"))
    print("Test 3 (Missing):", flexible_spell("Target3", "NoNumbersHere"))
    print("Test 4 (Insufficient):", flexible_spell("Target4", power=10))

    print("===============================================")
    print("\nTesting retrying spell...")
    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise ValueError("Boom")

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def waaaa_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(waaaa_spell())

    print("===============================================")
    print("\nTesting MageGuild...")
    guild = MageGuild()

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X"))

    print(guild.cast_spell("Lightning", power=15))

    print(guild.cast_spell("Fireball", power=5))
