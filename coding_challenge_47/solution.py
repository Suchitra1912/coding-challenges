# Coding Challenge 47: Find minimum value in an array
# Accept user input for array elements and find the minimum

# Input the number of elements
n = int(input("Enter the number of elements: "))

# Input each element and store in list
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

# Calculate minimum
minimum_value = min(arr)

# Display the result
print("Minimum value in the array:", minimum_value)
