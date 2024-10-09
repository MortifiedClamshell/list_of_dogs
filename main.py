"""
Module Docstring: main.py
======================
This is the main module of the read/write to text file project.
"""

__author__ = "Ash Williams"
__version__ = "0.1"
__date__ = "October 8, 2024"
__license__ = "None"

def read_file(file_name) -> None:
    """
    Reads a text file and prints it to the console.
    """
    try:
        with open(file_name, "r") as f:
            for line in f:
                print(line, end="")
    except FileNotFoundError:
        print(f"{file_name} not found.")

def new_file(file_name) -> None:
    """
    Creates a new file and writes data to it, or overwrites an existing file.
    """
    with open(file_name, "w") as f:
        f.write("Persian Shorthair\n")

def append_file(file_name, data) -> None:
    """
    Appends data to an existing file.
    """
    with open(file_name, "a") as f:
        with open(file_name, "r") as fr:
            lines = fr.readlines()
        if lines and lines[-1].strip() != "":
            f.write("\n")
        f.write(data.strip() + "\n")

def main():
    """
    Main entry point of the application.
    """
    while True:
        file_name = input("Enter the file name (or 'exit' to quit): ")
        if file_name.lower() == 'exit':
            break
        action = input("Do you want to read, create a new file, or append data? (read/new/append): ")
        if action.lower() == 'read':
            read_file(file_name)
        elif action.lower() == 'new':
            new_file(file_name)
        elif action.lower() == 'append':
            data = input("Enter the data to append: ")
            append_file(file_name, data)
        else:
            print("Invalid action. Please choose 'read', 'new', or 'append'.")

        print("\nContents of dogs.txt:")
        read_file("dogs.txt")
        print("\n")
        print("Contents of cats.txt:")
        read_file("cats.txt")
        print("\n")

if __name__ == "__main__":
    main()
