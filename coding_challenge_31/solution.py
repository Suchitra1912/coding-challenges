def calculate_final_amount(grand_total, payment_mode):
    """Apply surcharge based on payment mode."""
    surcharge = 0.0
    if payment_mode.lower() == "credit card":
        surcharge = grand_total * 0.02
    return grand_total + surcharge, surcharge


def main():
    grand_total = float(input("Enter grand total: "))
    payment_mode = input("Enter payment mode (Cash/Credit Card): ")
    
    final_total, surcharge = calculate_final_amount(grand_total, payment_mode)
    
    print(f"\nPayment Mode: {payment_mode}")
    print(f"Surcharge: ₹{surcharge:.2f}")
    print(f"Final Amount to Pay: ₹{final_total:.2f}")


if __name__ == "__main__":
    main()
