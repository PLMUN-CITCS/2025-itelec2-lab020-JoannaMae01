"""
Even or Odd Checker

This program prompts the user to enter an integer, validates the input, 
determines whether the number is even or odd, and displays the result.

Features:
- Function decomposition for modularity
- Input validation to ensure a valid integer is entered
- Uses the modulo operator (%) to check for even/odd numbers
"""

def get_integer_input() -> int:
    """
    Prompts the user to enter an integer and ensures valid input.

    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Error: Please enter a valid integer.")


def check_even_odd(number: int) -> str:
    """
    Determines if a given number is even or odd.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: A formatted message indicating whether the number is "Even" or "Odd".
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."


def main():
    """
    Main function to get the user's integer input, determine even/odd, and display the result.
    """
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)


if __name__ == "__main__":
    main()
