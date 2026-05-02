# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_harvest_total.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 19:30:24 by sekartav           #+#    #+#             #
#   Updated: 2026/04/20 14:00:46 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total() -> None:
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    Total = day1 + day2 + day3
    print("Total harvest", Total)
