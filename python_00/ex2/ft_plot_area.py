# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plot_area.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: sekartav <sekartav@student.42istanbul.com.tr+#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 19:30:21 by sekartav           #+#    #+#             #
#   Updated: 2026/04/20 14:00:54 by sekartav          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plot_area() -> None:
    length = int(input("Enter lenght: "))
    width = int(input("Enter width: "))
    area = length * width
    print("Plot area:", area)
