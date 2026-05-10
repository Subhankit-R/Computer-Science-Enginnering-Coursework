# Multiple built-in exceptions
def file_read(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    except PermissionError:
        print("Permission denied.")
