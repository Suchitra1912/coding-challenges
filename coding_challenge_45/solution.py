# Accept n elements from user and store in an array
def store_elements(n: int) -> list[int]:
    arr = []
    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        arr.append(num)
    return arr

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    array = store_elements(n)
    print("Array elements:", array)
