"""
Program: Leap Year Check
Author: Your Name
Date: YYYY-MM-DD
Description:
    Determines whether a given year is a leap year.
"""

def is_leap_year(year: int) -> bool:
    """
    Check leap year.

    Returns:
        bool: True if leap year, else False
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main():
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    except ValueError:
        print("Invalid input! Enter a valid year.")


if __name__ == "__main__":
    main()
