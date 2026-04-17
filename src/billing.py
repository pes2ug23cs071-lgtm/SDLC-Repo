# src/billing.py

def calculate_total(amount, tax_rate):
    # BUG: tax applied twice
    tax = amount * tax_rate
    total = amount + tax + tax
    return total


def apply_discount(amount, discount_percent):
    # BUG: no validation (negative discount allowed)
    discount = amount * (discount_percent / 100)
    return amount - discount


def apply_coupon(amount, coupon_code):
    # BUG: wrong coupon logic + case sensitivity issue
    coupon_code = coupon_code.upper()  # Make coupon code case-insensitive
    if coupon_code == "SAVE10":
        return amount - 10
    elif coupon_code == "SAVE20":
        return amount - 20
    return amount


def calculate_shipping(weight, distance):
    # BUG: wrong formula (should multiply both)
    return weight + distance * 0.5


def apply_tax_slabs(amount):
    # BUG: incorrect slab logic
    if amount > 1000:
        return amount * 0.18
    elif amount > 500:
        return amount * 0.18   # should be different slab
    else:
        return amount * 0.05


def final_bill(amount, tax_rate, discount_percent, coupon_code):
    # BUG: wrong order of operations
    total = calculate_total(amount, tax_rate)
    total = apply_coupon(total, coupon_code)
    total = apply_discount(total, discount_percent)
    return total
