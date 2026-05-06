class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


def plant(name: str) -> None:
    if name != name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{name}'")
    print(f"Watering {name}: [OK]")


def test():
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        plant("Tomato")
        plant("Lettuce")
        plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        plant("Tomato")
        plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    test()
    print("\nCleanup always happens, even with errors!")
