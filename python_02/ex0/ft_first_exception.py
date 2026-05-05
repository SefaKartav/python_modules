def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test() -> None:
    print("=== Garden Temperature ===\n")

    number = "25"
    print(f"Input data is '{number}'")

    try:
        temp = input_temperature(number)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    string = "abc"
    print(f"\nInput data is '{string}'")

    try:
        temp = input_temperature(string)
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test()
