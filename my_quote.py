"""
my_quote.py - Re-implementation of oracle shipping pricing engine.
"""

import math


def quote(weight_kg, distance_km, category, express=False, coupon=""):
    # 1. Round weight up to nearest 0.5 kg
    w = math.ceil(weight_kg * 2) / 2

    # 2. Base price formula (40 per kg + 2.5 per km)
    price = w * 40.0 + 2.5 * distance_km

    # 3. Category surcharges
    if category == "electronics":
        price *= 1.3
    elif category == "fragile":
        price += 150.0

    # 4. Express shipping fee
    if express:
        price += 80.0

    # 5. Coupon discount (WELCOME10)
    if coupon == "WELCOME10":
        price *= 0.9

    # 6. Minimum threshold
    if price < 100.0:
        price = 100.0

    # 7. Round to 2 decimals
    return round(price, 2)
