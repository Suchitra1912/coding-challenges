# ==============================
# HealWell Care Hospital System
# ==============================

GST_RATE = 0.18
SENIOR_DISCOUNT = 0.10
HIGH_BILL_DISCOUNT = 0.05


# ------------------------------
# Level 7: Admin sets services
# ------------------------------
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]


# ------------------------------
# Utility Functions
# ------------------------------
def display_services():
    print("\nAvailable Services:")
    for i in range(len(services)):
        print(f"{i + 1}. {services[i]} - ₹{costs[i]}")


def calculate_discounts(age, subtotal):
    discount = 0

    # Senior Citizen Discount
    if age >= 60:
        discount += subtotal * SENIOR_DISCOUNT

    # High Bill Discount (applied after senior discount)
    if subtotal - discount > 5000:
        discount += (subtotal - discount) * HIGH_BILL_DISCOUNT

    return discount


# ------------------------------
# Main Program
# ------------------------------
print("\n-----------------------------------------------")
print("Welcome to HealWell Care Hospital")
print("-----------------------------------------------")

# Level 1: Patient Details
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
contact = input("Enter Contact Number: ")

# Level 2: Service Selection
display_services()

choices = input(
    "\nEnter service numbers separated by commas (e.g., 1,4): "
).split(",")

selected_services = []
selected_costs = []

# Level 3: Fetch selected services & costs
for choice in choices:
    index = int(choice.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])
        selected_costs.append(costs[index])

# Level 4: Subtotal
subtotal = sum(selected_costs)

# Level 8: Discounts
discount = calculate_discounts(age, subtotal)
discounted_total = subtotal - discount

# Level 5: GST
gst = discounted_total * GST_RATE
grand_total = discounted_total + gst

# Level 6: Invoice Generation
print("\n-----------------------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("-----------------------------------------------")
print("Patient Information:")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Gender : {gender}")
print(f"Contact: {contact}")

print("\nServices Availed:")
for i in range(len(selected_services)):
    print(f"{i + 1}. {selected_services[i]} : ₹{selected_costs[i]}")

print("\n-----------------------------------------------")
print(f"Subtotal           : ₹{subtotal:.2f}")
print(f"Discount Applied   : ₹{discount:.2f}")
print(f"GST (18%)          : ₹{gst:.2f}")
print(f"Grand Total        : ₹{grand_total:.2f}")
print("-----------------------------------------------")
print("Thank you for choosing HealWell Care Hospital!")
print("-----------------------------------------------")
