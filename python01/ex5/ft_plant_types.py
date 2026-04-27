# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_types.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/07 00:53:31 by sekartav           #+#    #+#             #
#   Updated: 2026/03/07 02:35:42 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
        
    def get_info(self):
        return (f"{self.name} (Flower): {self.height}cm, {self.age} days, "
                f"{self.color} color")

        
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self):
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