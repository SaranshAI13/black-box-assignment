# SPEC.md - Pricing Rules Specification

## Overview of Pricing Rules

I tested quote() with different inputs and found the exact calculation steps used by the pricing engine:

---

### 1. Weight Rounding (Nearest 0.5 kg)

Weight is rounded up to the nearest 0.5 kg before calculation.

Formula: `w = ceil(weight_kg * 2) / 2`

Examples:
- 0.1 kg -> 0.5 kg
- 0.5 kg -> 0.5 kg
- 0.51 kg -> 1.0 kg
- 1.3 kg -> 1.5 kg

---

### 2. Base Price Calculation

Base price uses 40 per rounded kg and 2.5 per km:
`price = rounded_weight * 40.0 + distance_km * 2.5`

Example:
`quote(2.0, 100, "standard")` -> 2.0 * 40 + 100 * 2.5 = 330.0

---

### 3. Category Surcharges

- **electronics**: Multiply price by 1.3
- **fragile**: Add 150.0 flat fee
- **standard, books, clothing, food**: No change

---

### 4. Express Shipping Fee

If `express=True`, add 80.0 flat fee to the price.

---

### 5. Coupon Discount

If `coupon="WELCOME10"`, multiply total price by 0.9 (10% discount).

---

### 6. Minimum Price Floor & Rounding

- Minimum price threshold is 100.0 (price cannot fall below 100.0).
- Final output is rounded to 2 decimal places using `round(price, 2)`.
