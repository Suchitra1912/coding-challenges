"""
Program: Student Report Card
Author: Your Name
Date: YYYY-MM-DD
Description:
    Accepts a student's name and scores in three subjects.
    Calculates total, average, and class based on criteria.
"""

def calculate_class(scores: list[int]) -> str:
    """
    Calculate class based on average score.

    Parameters:
        scores (list[int]): List of three subject scores

    Returns:
        str: Class secured
    """
    if len(scores) != 3:
        raise ValueError("Exactly three scores are required.")

    total = sum(scores)
    average = total / 3

    if average >= 60:
        student_class = "1st Class"
    elif average >= 50:
        student_class = "2nd Class"
    elif average >= 35:
        student_class = "Pass Class"
    else:
        student_class = "Fail"

    return total, average, student_class


def main():
    try:
        name = input("Enter student name: ")
        scores = []
        for i in range(1, 4):
            score = float(input(f"Enter marks for subject {i}: "))
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100.")
            scores.append(score)

        total, average, student_class = calculate_class(scores)

        print(f"\nReport for {name}:")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Class: {student_class}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
