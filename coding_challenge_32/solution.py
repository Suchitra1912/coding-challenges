# solution.py
# Replace the function name and logic for each challenge

def challenge_function(input_value):
    """
    Process input_value according to challenge logic and return result
    """
    if input_value < 0:
        raise ValueError("Input must be non-negative")
    # Example logic: square the number
    result = input_value ** 2
    return result

# Optional: run standalone
if __name__ == "__main__":
    try:
        val = int(input("Enter a value: "))
        print("Result:", challenge_function(val))
    except ValueError as e:
        print("Error:", e)
