# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_growth.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/06 21:20:56 by sekartav           #+#    #+#             #
#   Updated: 2026/04/22 14:04:28 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height += 0.8

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


def simulate(plant: Plant) -> None:
    print("=== Garden Plant Growth ===")
    firs_height = plant.height
    plant.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    last_height = plant.height
    growth = round(last_height - firs_height, 1)
    print(f"Growth this week: {growth:.1f}cm")



if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    simulate(rose)
