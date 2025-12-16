def calculate_tax(income):
    """
    Calculates tax payable under New Tax Regime (2023),
    including Section 87A rebate and 4% cess.
    Returns a detailed breakdown.
    """

    tax = 0
    breakdown = []

    slabs = [
        (300000, 0.00),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)
    ]

    prev_limit = 0
    remaining_income = income

    for limit, rate in slabs:
        if income > prev_limit:
            taxable = min(remaining_income, limit - prev_limit)
            slab_tax = taxable * rate
            tax += slab_tax
            breakdown.append((prev_limit + 1, limit, rate * 100, slab_tax))
            remaining_income -= taxable
            prev_limit = limit
        else:
            break

    # Section 87A Rebate
    rebate = 0
    if income <= 700000:
        rebate = tax
        tax = 0

    cess = tax * 0.04
    total_tax = tax + cess

    return {
        "income": income,
        "tax_before_rebate": tax + rebate,
        "rebate": rebate,
        "tax_after_rebate": tax,
        "cess": cess,
        "total_tax": total_tax,
        "breakdown": breakdown
    }


if __name__ == "__main__":
    income = float(input("Enter your annual taxable income (₹): "))

    result = calculate_tax(income)

    print("\n--- Tax Breakdown (New Tax Regime 2023) ---")
    print(f"Taxable Income: ₹{result['income']:.2f}")
    print("\nSlab-wise Tax:")
    for start, end, rate, tax in result["breakdown"]:
        if tax > 0:
            print(f"₹{start} - ₹{end} @ {rate}% : ₹{tax:.2f}")

    print(f"\nTax Before Rebate: ₹{result['tax_before_rebate']:.2f}")
    print(f"Section 87A Rebate: ₹{result['rebate']:.2f}")
    print(f"Tax After Rebate: ₹{result['tax_after_rebate']:.2f}")
    print(f"Health & Education Cess (4%): ₹{result['cess']:.2f}")
    print(f"Total Tax Payable: ₹{result['total_tax']:.2f}")
