import difflib

def main():
    target_string = input("Enter the name of a switch game: ")
    
    database = game_list_to_list(".\\game_list\\nintendo_switch_game_list.txt")
    print(find_closest_approximation(target_string, database))

def find_closest_approximation(target_string, database):
    """Finds the closest approximation of a target string within a database of strings.

    Args:
        target_string (str): The string to find an approximation for.
        database (list): A list of strings to search within.

    Returns:
        str: The closest approximation found in the database.
        None: If no suitable approximation is found.
    """

    closest_matches = difflib.get_close_matches(target_string, database, n=1, cutoff=0.6)

    if closest_matches:
        return closest_matches[0]  # Return the best match
    else:
        print(f"No close approximations found for '{target_string}' in the database.")
        return None

def game_list_to_list(filename):
    """
    Reads lines from a text file into a list of strings.

    Args:
        filename: The path to the text file.

    Returns:
        A list of strings, where each element is a line from the file.
    """

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    main()