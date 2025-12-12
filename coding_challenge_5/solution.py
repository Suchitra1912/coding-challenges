"""
Program: Farmer Sales Calculation
Author: Your Name
Date: YYYY-MM-DD
Description:
    Calculates overall sales and sales from chemical-free farming for Mahesh's 80-acre farm.
"""

def calculate_sales():
    # Land per segment
    total_land = 80
    segment_area = total_land / 5  # 16 acres per segment

    # Crop yields and prices
    tomato_area = segment_area
    potato_area = segment_area
    cabbage_area = segment_area
    sunflower_area = segment_area
    sugarcane_area = segment_area

    # Tomatoes
    tomato_yield = 0.3 * tomato_area * 10 + 0.7 * tomato_area * 12  # tonnes
    tomato_kg = tomato_yield * 1000
    tomato_sale = tomato_kg * 7  # Rs

    # Potatoes
    potato_yield = 10 * potato_area  # tonnes
    potato_kg = potato_yield * 1000
    potato_sale = potato_kg * 20

    # Cabbage
    cabbage_yield = 14 * cabbage_area
    cabbage_kg = cabbage_yield * 1000
    cabbage_sale = cabbage_kg * 24

    # Sunflower
    sunflower_yield = 0.7 * sunflower_area
    sunflower_kg = sunflower_yield * 1000
    sunflower_sale = sunflower_kg * 200

    # Sugarcane
    sugarcane_yield = 45 * sugarcane_area
    sugarcane_sale = sugarcane_yield * 4000  # Rs

    # Overall sales
    total_sales = tomato_sale + potato_sale + cabbage_sale + sunflower_sale + sugarcane_sale

    # Chemical-free sales at 11 months (all crops converted)
    chemical_free_sales = total_sales

    print(f"Overall Sales from 80 acres: Rs {total_sales:,.0f}")
    print(f"Sales from Chemical-Free Farming at 11 months: Rs {chemical_free_sales:,.0f}")


if __name__ == "__main__":
    calculate_sales()
