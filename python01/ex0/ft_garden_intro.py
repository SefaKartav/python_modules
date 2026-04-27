# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_intro.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/06 20:40:16 by sekartav           #+#    #+#             #
#   Updated: 2026/04/21 15:07:25 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_garden_intro() -> None:
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
