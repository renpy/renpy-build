# Updates a catalog of the game files and their MD5 hash sums. 
# This is used by the PWA service worker to check if the files have changed and need to be re-downloaded.
# Please run this script from the root directory of the build whenever you make changes to the
# game files (e.g. images, sounds, etc.) manually AFTER you have built the game. Otherwise, the
# service worker will not be able to detect the changes and will not update the files.
# This script is not needed if you use the Ren'Py launcher to build the game.
# Python 3.6 or higher is required to run this script.
import hashlib
import os
import json

def get_md5_hash(file_path: str) -> str:
    """
    Generates MD5 hash sum of the given file.

    :param file_path: string, The path to the file.

    :return: string, The MD5 hash sum of the file.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} was not found.")

    # Check if the file is not a directory
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"The file {file_path} is a directory.")

    # Check if the file is not empty
    if os.stat(file_path).st_size == 0:
        raise ValueError(f"The file {file_path} is empty.")

    # Create a new MD5 hash object
    md5_hash = hashlib.md5()
    # Open the file in read byte mode
    with open(file_path, "rb") as file:
        # Read the file in 4KB chunks
        for chunk in iter(lambda: file.read(4096), b""):
            # Update the hash with the current chunk
            md5_hash.update(chunk)

    # Return the hash as a string
    return md5_hash.hexdigest()


def main():
    """
    It walks through the game folder, gets the MD5 hash of each file, and adds it to the catalog
    """
    # Check if pwa_catalog.json exists
    if not os.path.exists("pwa_catalog.json"):
        raise FileNotFoundError("The file pwa_catalog.json was not found. Please run this script from the root directory of the build.")

    # Read current catalog
    with open("pwa_catalog.json", "r") as f:
        catalog = json.load(f)
    
    catalog_files = {}
    # Get current directory
    destination = os.path.dirname(os.path.realpath(__file__))
    # Walk through the game folder
    for root, dirs, files in os.walk(os.path.join(destination, "game")):
        for file in files:
            # Get the absolute path of the file
            file_path = os.path.join(root, file)
            # Convert it to relative path of the file
            file_name = os.path.relpath(file_path, destination)
            # Replace backslashes with forward slashes
            file_name = file_name.replace("\\", "/")
            # Get the MD5 hash of the file
            file_hash = get_md5_hash(file_path)
            # Add the file to the catalog
            catalog_files[file_hash] = file_name
    

    # Update catalog
    catalog["files"] = catalog_files

    # Write new catalog
    with open("pwa_catalog.json", "w") as f:
        f.write(json.dumps(catalog, separators=(',', ':')))


if __name__ == "__main__":
    main()
