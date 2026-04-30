# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_types.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/07 00:53:31 by sekartav           #+#    #+#             #
#   Updated: 2026/04/30 20:15:39 by sekartav          ###   ########.fr       #
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
        if h >= 0:
            self._height = h

    def set_age(self, a: int) -> None:
        if a >= 0:
            self._days_age = a
        
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_age

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
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self.get_height():.1f}cm long and "
               f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

        
class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

if __name__ == "__main__":
    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("\n[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("\n[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show()

    print("\n=== Vegetable ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("\n[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.age()
        tomato.grow()