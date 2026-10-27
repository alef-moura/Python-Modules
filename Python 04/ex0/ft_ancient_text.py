#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        # open() devolve um objeto de arquivo (io.TextIOWrapper)
        file: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    try:
        content = file.read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file '{filename}': {error}")
        content = ""
    file.close()  # sem 'with', precisamos fechar manualmente
    print("---")
    print(content, end="")
    print("---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
