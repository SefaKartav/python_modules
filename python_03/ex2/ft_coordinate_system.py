import math


def get_player_pos():

    while (True):
        user_ip = input("Enter new coordinates as floats in format 'x,y,z': ")
        splits = user_ip.split(",")

        if len(splits) != 3:
            print("Invalid syntax")
            continue

        coords = []
        error_alert = False

        for i in splits:
            new = i.strip()
            try:
                coords += [float(new)]
            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                error_alert = True
                break

        if not error_alert:
            return tuple(coords)


def main():
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print("Distance between the 2 sets of"
          f"coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    main()
