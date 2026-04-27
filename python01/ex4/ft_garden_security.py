# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_security.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/06 23:54:52 by sekartav           #+#    #+#             #
#   Updated: 2026/04/22 19:56:33 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name
        self._height = 0.0
        self._days_age = 0

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_days_age) -> None:
        if new_days_age < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._days_age = new_days_age

    def get_age(self) -> None:
        return self._days_age

    def show(self) -> None:
        print(f"Current state: {self.name}: {self._height}cm, {self._days_age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)

    print("Height updated: 25cm")
    rose.set_height(25.0)

    print("Age updated: 30 days")
    rose.set_age(30)

    rose.set_height(-5.0)
    rose.set_age(-10)
    rose.show()
