def calculate_total(amount, tax_rate):
    # BUG: tax is applied twice
    tax = amount * tax_rate
    total = amount + tax
    return total

def apply_surge_pricing(amount, surge_multiplier):
    return amount * surge_multiplier

def apply_discount(amount, discount_percent):
    discount = amount * (discount_percent / 100)
    return amount - discount
