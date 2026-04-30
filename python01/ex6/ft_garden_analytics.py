# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_analytics.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/30 15:08:50 by sekartav           #+#    #+#             #
#   Updated: 2026/04/30 20:17:24 by sekartav          ###   ########.fr       #
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
        self.name = name
        self.height = height
        self.age = age
        self._stats = self.__Stats()

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
        pass

    @classmethod
    def create_object(cls):
        pass


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
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self._shade_count = 0

    def produce_shade(self) -> None:
        self._shade_count += 1
        print(f"Tree {self.name} now produces a shade of {self.get_height():.1f}cm long and "
               f"{self.trunk_diameter:.1f}cm wide.")
               
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def get_shade_count(self) -> int:
        return self._shade_count