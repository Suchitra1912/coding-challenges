# Coding Challenge 39: Perfect Squares with Alternating Signs Pattern

def square_pattern(n):
    if n <= 0:
        return "Error"

    num = 1
    result = []

    for row in range(1, n + 1):
        current = []
        for _ in range(row):
            square = num * num
            # Alternate sign based on square index
            if num % 2 == 0:
                square = -square
            current.append(str(square))
            num += 1
        result.append(" ".join(current))

    return result
