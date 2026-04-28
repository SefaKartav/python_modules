# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_types.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/07 00:53:31 by sekartav           #+#    #+#             #
#   Updated: 2026/04/28 18:19:59 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name
        self._height = height
        self._days_age = days_age
        self.set_height(height)
        self.set_age(days_age)
        
        def set_height(self, h: float) -> None:
            self._height = h if h >= 0 else self._height

        def set_age(self, a: int) -> None:
            self._days_age = a if a >= 0 else self._days_age

        def grow(self) -> None:
            self._height += 0.8

        def age(self) -> None:
            self._days_age += 1
    
        def show(self) -> None:
            print(f"{self.name}: {self._height:.1f}cm, {self._days_age} days old")

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True
        
    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

        
class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self) -> None:
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}")

        
class Vegateble(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_ntrv(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
                f"{self.harvest_season} harvest")

def ft_plant_harvest():
    rose = Flower("Rose", 25, 30, "red")
    
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegateble("Tomato", 80, 90, "summer", "vitamin C")

    g