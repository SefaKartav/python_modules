# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_count_harvest_recursive.py                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 19:40:07 by sekartav           #+#    #+#             #
#   Updated: 2026/04/20 14:00:02 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive(now: int | None = None,
                               start: int = 1) -> None:
    if now is None:
        now = int(input("Days until harvest: "))
    if now >= start:
        print(f"Day {start}")
        ft_count_harvest_recursive(now, start + 1)
    if now == start:
        print("Harvest time!")
