#!/usr/bin/env python3
import sys
import typing


def read_file(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return None
    try:
        content = file.read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file '{filename}': {error}")
        content = ""
    file.close()
    print("---")
    print(content, end="")
    print("---")
    print(f"File '{filename}' closed.")
    return content


def transform(content: str) -> str:
    result = ""
    for line in content.splitlines():
        result += line + "#\n"
    return result


def save_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    try:
        # modo "w": cria o arquivo ou substitui o existente
        file: typing.IO[str] = open(filename, "w")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        print("Data not saved.")
        return
    try:
        file.write(content)
    except OSError as error:
        print(f"Error writing file '{filename}': {error}")
        print("Data not saved.")
        file.close()
        return
    file.close()
    print(f"Data saved in file '{filename}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = read_file(sys.argv[1])
    if content is None:
        return
    new_content = transform(content)
    print("\nTransform data:")
    print("---")
    print(new_content, end="")
    print("---")
    target = input("Enter new file name (or empty): ")
    if target == "":
        print("Not saving data.")
        return
    save_file(target, new_content)


if __name__ == "__main__":
    main()
