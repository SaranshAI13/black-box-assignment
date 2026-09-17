"""
probes.py - Test probes used to deduce pricing rules.
"""

from oracle import quote, queries_used, reset_counter

reset_counter()

print("--- Sanity Check ---")
print("quote(2.0, 100, 'standard') =", quote(2.0, 100, 'standard'))

print("\n--- Weight Tests ---")
for w in [0.1, 0.5, 1.0, 1.5, 2.0]:
    print(f"w={w} -> {quote(w, 100, 'standard')}")

print("\n--- Distance Tests ---")
for d in [1, 10, 50, 100, 200]:
    print(f"d={d} -> {quote(1.0, d, 'standard')}")

print("\n--- Category Tests ---")
for cat in ["standard", "electronics", "fragile", "books", "clothing", "food"]:
    print(f"{cat} -> {quote(2.0, 100, cat)}")

print("\n--- Express Test ---")
print("express=False ->", quote(2.0, 100, 'standard', express=False))
print("express=True  ->", quote(2.0, 100, 'standard', express=True))

print("\n--- Coupon Test ---")
print("No coupon ->", quote(2.0, 100, 'standard'))
print("WELCOME10 ->", quote(2.0, 100, 'standard', coupon='WELCOME10'))

print("\nQueries used:", queries_used())
