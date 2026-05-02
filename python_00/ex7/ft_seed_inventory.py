# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_seed_inventory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/20 13:21:10 by sekartav           #+#    #+#             #
#   Updated: 2026/04/20 13:56:39 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed} seeds: {quantity} packets avaliable")
    elif unit == "grams":
        print(f"{seed} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed} seeds: covers {quantity} quare meters")
    else:
        print("Unknown unit type")
