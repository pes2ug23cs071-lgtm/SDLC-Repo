def calculate_total(amount, tax_rate):
    # BUG: tax is applied twice
    tax = amount * tax_rate
    total = amount + tax + tax
    return total

def apply_discount(amount, discount_percent):
    discount = amount * (discount_percent / 100)
    return amount - discount
