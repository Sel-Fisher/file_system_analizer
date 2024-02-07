import os
import stat
import mimetypes
import argparse


def classify_file_type(file_path):
    """Classify file into categories based on extension or file signatures."""
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type.split("/")[0] if mime_type else "unknown"


def analyze_directory(directory_path, size_threshold: int = 0):
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

                if file_permissions & stat.S_IWOTH:
                    world_writable_files.append(file_path)

                if file_size > size_threshold:
                    large_files.append((file_path, file_size))

            except (OSError, PermissionError) as e:
                print(f"Error accessing {file_path}: {e}")

    print("\nSize analysis:")
    for file_type, total_size in file_types.items():
        print(f"{file_type}: {total_size / 1024 / 1024:.2f} MB")

    print("\nLarge files:")
    for file_path, file_size in large_files:
        print(f"{file_path}: {file_size / 1024 / 1024:.2f} MB")

    print("\nWorld-Writable Files:")
    for file_path in world_writable_files:
        print(file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze file system structure and usage.")
    parser.add_argument("directory", type=str, help="The directory path to analyze.")
    parser.add_argument("--size_threshold", type=int, default=0, help="The size threshold for large files (in bytes).")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a directory.")
    else:
        analyze_directory(args.directory, args.size_threshold)
