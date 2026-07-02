import sys
import typing


def get_line(file_path: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_path}'")
    try:
        file: typing.IO = open(file_path, "r")
        contents: str = file.read()
        print(contents, end="")
        print("\n")
        file.close()
        print(f"File '{file_path}' closed.")

    except FileNotFoundError:
        print(f"Error opening file '{file_path}': "
              f"[Errno 2] No such file or diractory: '{file_path}'")

    except PermissionError:
        print(f"Error opening file '{file_path}': "
              f"[Errno 13] Permission denied: '{file_path}'")

    except Exception as i:
        print(f"Error opening file '{file_path}': {i}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        get_line(sys.argv[1])
