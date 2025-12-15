def apply_promotional_discount(items, promo_code="PROMO10", discount_percent=10):
    grand_total = 0.0
    for item in items:
        total = item["quantity"] * item["price"]
        if item["code"] == promo_code:
            total *= (1 - discount_percent / 100)
        grand_total += total
    return grand_total


def main():
    n = int(input("Enter number of items: "))
    items = []
    for _ in range(n):
        code = input("Enter item code: ")
        desc = input("Enter description: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        items.append({"code": code, "description": desc, "quantity": qty, "price": price})

    grand_total = apply_promotional_discount(items)
    print(f"\nGrand Total after promotional discounts: ₹{grand_total:.2f}")


if __name__ == "__main__":
    main()
