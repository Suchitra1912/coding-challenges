# Coding Challenge 49: Search for an element in an array

# Input the number of elements
n = int(input("Enter the number of elements: "))

# Input array elements
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

# Input element to search
search_val = int(input("Enter the element to search: "))

# Search the element
if search_val in arr:
    index = arr.index(search_val)
    print(f"Element {search_val} found at index {index} (0-based).")
else:
    print(f"Element {search_val} not found in the array.")
