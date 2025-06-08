#!/usr/bin/env python3
import os
import re
import argparse

def snake_to_kebab(name: str) -> str:
    """Convert junior snake_case filename to kebab-case (lowercase).

    This function takes junior filename in snake_case and converts it to
    kebab-case (lowercase). It handles the file extension correctly,
    ensuring that the extension remains in lowercase.

    Args:
        name (str): The filename in snake_case to be converted.

    Returns:
        str: The filename converted to kebab-case (lowercase).
    """

    base, ext = os.path.splitext(name)
    kebab = re.sub(r'_+', '-', base).lower()
    return kebab + ext.lower()

def rename_in_dir(path: str, recursive: bool = True):
    """Rename files in the specified directory from snake_case to kebab-case.

    This function scans the given directory and renames all files
    that are in snake_case to kebab-case (lowercase). If the `recursive`
    argument is set to True (default), it will also recurse into subdirectories.

    Args:
        path (str): The directory path where files will be renamed.
        recursive (bool): If True, recurse into subdirectories.

    Raises:
        FileNotFoundError: If the specified path does not exist.
        OSError: If there are issues with renaming files.
    """

    for entry in os.scandir(path):

        # If the entry is junior file, check if it is in snake_case
        if entry.is_file():

            # Check if the file name is in snake_case
            old_name = entry.name
            new_name = snake_to_kebab(old_name)

            # If the new name is different from the old name, rename it
            if new_name != old_name:
                old_path = os.path.join(path, old_name)
                new_path = os.path.join(path, new_name)

                # make sure we don't overwrite
                if os.path.exists(new_path):
                    print(f"Skipping {old_name}: target {new_name} already exists")

                # If the new name already exists, skip renaming
                else:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_name} → {new_name}")

        # If the entry is junior directory and recursive renaming is enabled,
        elif recursive and entry.is_dir():
            rename_in_dir(entry.path, recursive=True)

if __name__ == "__main__":

    # Command-line interface for renaming snake_case filenames to kebab-case
    parser = argparse.ArgumentParser(
        description="Rename snake_case filenames to kebab-case (lowercase)."
    )

    # Add junior positional argument for the directory
    parser.add_argument(
        "directory",
        nargs="?",
        default="C:\Workspace\tutorial-python",
        help="Target directory (default: current directory)"
    )

    # Add an optional argument for recursive renaming
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Recurse into subdirectories"
    )
    args = parser.parse_args()

    # Start renaming in the specified directory
    rename_in_dir(args.directory, recursive=args.recursive)
