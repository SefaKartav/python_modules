import sys
import typing


def get_line(file_path: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_path}'")
    print("---\n")
    try:
        file: typing.IO = open(file_path, "r")
        contents: str = file.read()
        print(contents, end="")
        print("\n")
        file.close()
        print("---")
        print(f"File '{file_path}' closed.\n")

    except FileNotFoundError:
        print(f"[STDERR] Error opening file '{file_path}': "
              f"[Errno 2] No such file or directory: "
              f"'{file_path}'", file=sys.stderr)
        return

    except PermissionError:
        print(f"[STDERR] Error opening file '{file_path}': "
              f"[Errno 13] Permission denied: '{file_path}'", file=sys.stderr)
        return

    except Exception as i:
        print(f"[STDERR] Error opening file "
              f"'{file_path}': {i}", file=sys.stderr)
        return

    print("Transform data:")
    print("---\n")
    transformed_content = ""
    for line in contents.splitlines():
        new_line = (f"{line}#")
        print(new_line)
        transformed_content += new_line + "\n"

    print("Enter new file name (or empty):", end="")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip('\n')

    if not new_file:
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_file}'")
        try:
            for_new_line: typing.IO = open(new_file, "w")
            for_new_line.write(transformed_content)
            for_new_line.close()
            print(f"Data saved in file '{new_file}'.")
        except Exception as i:
            print(f"[STDERR] Error saving file: {i}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
    else:
        get_line(sys.argv[1])
