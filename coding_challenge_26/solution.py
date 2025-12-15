"""
Coding Challenge 26: Iterative Item Entry and Grand Total
Calculates grand total for multiple items.
"""

def compute_grand_total(items: list[dict]) -> float:
    """
    Compute grand total from a list of items.
    Each item is a dictionary with keys: code, desc, qty, price
    """
    grand_total = 0
    for item in items:
        total = item["qty"] * item["price"]
        grand_total += total
    return grand_total


def main():
    items = []
    print("Enter item details (leave code empty to stop):")
    while True:
        code = input("Item Code: ")
        if not code:
            break
        desc = input("Description: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        items.append({"code": code, "desc": desc, "qty": qty, "price": price})

    grand_total = compute_grand_total(items)
    print(f"\nGrand Total: {grand_total}")


if __name__ == "__main__":
    main()
