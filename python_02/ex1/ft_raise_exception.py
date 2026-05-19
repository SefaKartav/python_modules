def input_temperature(temp_str: str) -> int:
    tmp = int(temp_str)

    if tmp > 40:
        raise Exception(f"{tmp}°C is too hot for plants (max 40°C)")
    elif tmp < 0:
        raise Exception(f"{tmp}°C is too cold for plants (min 0°C)")

    return tmp


def test_temperature() -> None:
    cases = ['25', 'abc', '100', '-50']

    for data in cases:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}°C\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
