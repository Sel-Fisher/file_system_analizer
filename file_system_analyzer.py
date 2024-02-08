#!/usr/bin/env python3

import os
import mimetypes
import argparse


def classify_file_type(file_path: str) -> str:
    """Classify file into categories based on extension or file signatures."""
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type.split("/")[0] if mime_type else "unknown"


def analyze_directory(
    directory_path: str, size_threshold: int, show_world_writable: bool = False
) -> None:
    """Analyze the file system structure and usage."""
    file_types = {}
    large_files = []
    world_writable_files = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                file_type = classify_file_type(file_path)
                file_types[file_type] = file_types.get(file_type, 0) + file_size
                file_permissions = os.stat(file_path).st_mode

                if os.access(file_path, os.W_OK):
                    world_writable_files.append(file_path)

                if file_size > size_threshold:
                    large_files.append((file_path, file_size))

            except (OSError, PermissionError) as e:
                print(f"Error accessing {file_path}: {e}")

    print("\nSize analysis:")
    for file_type, total_size in file_types.items():
        print(f"{file_type}: {total_size / 1024 / 1024:.2f} MB")

    print("\nLarge files:")
    if large_files:
        for file_path, file_size in large_files:
            print(f"{file_path}: {file_size / 1024 / 1024:.2f} MB")
    else:
        print(f"There is no files larger than {size_threshold / 1024 / 1024:.2f} MB")

    if show_world_writable:
        print("\nWorld-Writable Files:")
        if world_writable_files:
            for file_path in world_writable_files:
                print(file_path)
        else:
            print("There is no World-Writable Files!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze file system structure and usage."
    )
    parser.add_argument(
        "directory",
        type=str,
        help="The directory path to analyze."
    )
    parser.add_argument(
        "-s",
        "--size-threshold",
        type=int,
        default=1048576,
        help="The size threshold for large files (in bytes).",
    )
    parser.add_argument(
        "-w",
        "--show-world-writable",
        action="store_true",
        help="Show world-writable files."
    )
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a directory.")
    else:
        analyze_directory(args.directory, args.size_threshold, args.show_world_writable)
