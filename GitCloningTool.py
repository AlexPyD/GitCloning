import os
import subprocess

def clone_repository():
    # Prompt the user for the repository URL
    repository_url = input("Enter the GitHub repository URL: ")
    
    # Prompt the user for the destination path
    clone_destination = input("Enter the destination path for cloning: ")

    # Check if the destination directory already exists
    if os.path.exists(clone_destination):
        print(f"Destination directory '{clone_destination}' already exists.")
        return

    # Run the git clone command
    try:
        subprocess.run(["git", "clone", repository_url, clone_destination], check=True)
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while cloning the repository: {e}")

clone_repository()
