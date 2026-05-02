# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_water_reminder.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 19:30:31 by sekartav           #+#    #+#             #
#   Updated: 2026/04/20 14:00:29 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder() -> None:
    day = int(input("Days since last watering: "))
    if (day > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
