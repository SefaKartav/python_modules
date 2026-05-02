# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_age.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 19:30:28 by sekartav           #+#    #+#             #
#   Updated: 2026/04/20 14:00:37 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plant_age() -> None:
    age = int(input("Enter plant age in days:"))
    if (age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")
