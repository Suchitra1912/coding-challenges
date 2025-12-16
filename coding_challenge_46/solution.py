# Coding Challenge 46: Find the sum of all elements in an array
# Accept user input for array elements and calculate sum

# Input the number of elements
n = int(input("Enter the number of elements: "))

# Input each element and store in list
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

# Calculate sum
total_sum = sum(arr)

# Display the result
print("Sum of all elements:", total_sum)
