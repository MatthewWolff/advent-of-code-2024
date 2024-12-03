import pandas as pd


def parse_two_columns(file_path, delimiter='   '):
    """
    Parses a text file with two columns of integers separated by a specified delimiter.

    Parameters:
        file_path (str): Path to the text file to parse.
        delimiter (str): Delimiter separating the two columns. Default is three spaces.

    Returns:
        list[tuple[int, int]]: A list of tuples containing the integers from the two columns.
    """
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    parts = line.split(delimiter)
                    if len(parts) == 2:
                        col1 = int(parts[0].strip())
                        col2 = int(parts[1].strip())
                        data.append((col1, col2))
                    else:
                        raise ValueError(f"Invalid line format: {line.strip()}")
        return zip(*data)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError as e:
        print(f"Error: {e}")


def parse_matrix(file_path):
    """
    Reads a text file where each row contains numbers separated by spaces
    and returns a list of lists of integers.

    Parameters:
        file_path (str): Path to the text file.

    Returns:
        list[list[int]]: A list of lists of integers.
    """
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    row = [int(num) for num in line.split()]
                    numbers.append(row)
        return numbers
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError as e:
        print(f"Error: {e}")


def parse_numbers_from_string(input_string):
    """
    Parses a string where each row contains numbers separated by spaces
    and returns a list of lists of integers.

    Parameters:
        input_string (str): The input string.

    Returns:
        list[list[int]]: A list of lists of integers.
    """
    numbers = []
    try:
        for line in input_string.strip().split("\n"):
            if line.strip():  # Skip empty lines
                row = [int(num) for num in line.split()]
                numbers.append(row)
        return numbers
    except ValueError as e:
        print(f"Error: {e}")


def read_file_as_list(file_path):
    """
    Reads a text file and returns its contents as a list of strings.

    Parameters:
        file_path (str): Path to the text file.

    Returns:
        list[str]: A list of strings, each representing a line in the file.
    """
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except IOError as e:
        print(f"Error reading file: {e}")
        return []
