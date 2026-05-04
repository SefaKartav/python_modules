class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name
        self.height = height
        self.days_age = days_age

    def age(self) -> None:
        self.days_age += 1

    def grow(self) -> None:
        self.height += 0.8

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_age} days old")


def ft_plant_factory() -> None:
    plant_data = [
          ("Rose", 25.0, 30),
          ("Oak", 200.0, 365),
          ("Cactus", 5.0, 90),
          ("Sunflower", 80.0, 45),
          ("Fern", 15.0, 120)
    ]

    print("=== Plant Factory Output ===")

    for data in plant_data:
        plant = Plant(*data)
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
