from src.billing import calculate_total, apply_discount

def test_calculate_total():
    assert calculate_total(100, 0.1) == 110.0

def test_apply_discount():
    assert apply_discount(100, 10) == 90.0
