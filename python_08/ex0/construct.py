import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def print_warning() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("Then run this program again.")


def print_venv_success() -> None:
    venv_name: str = os.path.basename(sys.prefix)
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")

    try:
        packages_path: list[str] = site.getsitepackages()
        if packages_path:
            print(packages_path)
    except Exception as e:
        print(f"Error retrieving package path: {e}")


if __name__ == "__main__":
    try:
        if is_virtual_env():
            print_venv_success()
        else:
            print_warning()
    except Exception as e:
        print(f"Matrix glitch detected: {e}")
