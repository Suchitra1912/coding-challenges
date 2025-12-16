# Coding Challenge 52: Reverse an array

# Input number of elements
n = int(input("Enter the number of elements: "))

# Input array elements
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

# Reverse the array
reversed_arr = arr[::-1]

# Display reversed array
print("Reversed Array:", reversed_arr)
