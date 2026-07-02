import sys


def scan_inventory(args: list[str]) -> dict[str, int]:
    dictionary: dict[str, int] = {}

    for i in args:
        if ":" not in i:
            print(f"Error - invalid parameter '{i}'")
            continue
        cut = i.split(":")

        if len(cut) != 2:
            print(f"Error - invalid parameter '{i}'")
            continue

        name = cut[0]
        value = cut[1]

        if name in dictionary.keys():
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            check = int(value)
            dictionary[name] = check
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    return dictionary


def main():
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    new_dictionary = scan_inventory(args)
    item_list = list(new_dictionary.keys())
    key_count = len(item_list)
    item_count = sum(new_dictionary.values())
    most_item = max(new_dictionary.values())
    least_item = min(new_dictionary.values())
    most_name = max(new_dictionary, key=new_dictionary.get)
    least_name = min(new_dictionary, key=new_dictionary.get)

    print(f"Got inventory: {new_dictionary}")
    print(f"Item list: {item_list}")
    print(f"Total quantity of the {key_count} items: {item_count}")
    for i in new_dictionary:
        counter = new_dictionary[i]
        ratio = round((counter / item_count) * 100, 1)
        print(f"Item {i} represent {ratio}%")

    print(f"Item most abundant: {most_name} with quantity {most_item}")
    print(f"Item least abundant: {least_name} with quantity {least_item}")
    new_dictionary.update({"magic_item": 1})
    print(f"Got inventory: {new_dictionary}")


if __name__ == "__main__":
    main()
