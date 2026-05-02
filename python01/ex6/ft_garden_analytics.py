# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_analytics.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/30 15:08:50 by sekartav           #+#    #+#             #
#   Updated: 2026/05/02 18:46:48 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    class __Stats:
        def __init__(self):
            self.__grow_count = 0
            self.__age_count = 0
            self.__show_count = 0

        def add_grow_count(self) -> None:
            self.__grow_count += 1

        def add_age_count(self) -> None:
            self.__age_count += 1

        def add_show_count(self) -> None:
            self.__show_count += 1

        def get_stats(self) -> str:
            return (f"{self.__grow_count} grow, "
                    f"{self.__age_count} age, {self.__show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = self.__Stats()

    def get_stats(self) -> str:
        return self._stats.get_stats()

    def grow(self) -> None:
        self._height += 8.0
        self._stats.add_grow_count()

    def age(self) -> None:
        self._age += 1
        self._stats.add_age_count()

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._stats.add_show_count()

    @staticmethod
    def is_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_object(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self._name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self._shade_count = 0

    def produce_shade(self) -> None:
        self._shade_count += 1
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def get_shade_count(self) -> int:
        return self._shade_count


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistic(plant_obj) -> None:
    print(f"Stats: {plant_obj.get_stats()}")
    if isinstance(plant_obj, Tree):
        print(f"{plant_obj.get_shade_count()} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("--- Check year-old ---")
    print(f"Is 30 days more than a year? -> {Plant.is_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_a_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_statistic(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistic(rose)

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_statistic(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistic(oak)

    print("\n=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.bloom()
    sunflower.age()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistic(sunflower)

    print("=== Anonymous")
    unknow = Plant.create_object()
    unknow.show()
    print("[statistics for Unknown plant]")
    display_statistic(unknow)
