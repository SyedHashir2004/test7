"""
Module for multiplication operations.
"""

def multiply(first_number: int, second_number: int) -> int:
    """
    Multiply two numbers.

    :param first_number: The first number.
    :param second_number: The second number.
    :return: The product of the two numbers.
    """
    result = first_number * second_number
    return result

if __name__ == "__main__":
    # First number
    A = 1
    # Second number
    B = 2
    # Multiplication of the two numbers
    L = multiply(A, B)
    # Printing the result
    print(f"The product of {A} and {B} is {L}")
