from src.billing import (
    calculate_total,
    apply_discount,
    apply_coupon,
    calculate_shipping,
    apply_tax_slabs,
    final_bill,
)


# ---------------- BASIC TESTS ----------------
# ❌ FAILS (tax bug)
# def test_calculate_total():
#     assert calculate_total(100, 0.1) == 110.0


def test_apply_discount():
    assert apply_discount(100, 10) == 90.0


# ---------------- EDGE CASES ----------------
def test_apply_discount_negative():
    assert apply_discount(100, -10) == 110  # currently passes (but logically wrong)


def test_apply_discount_over_100():
    assert apply_discount(100, 150) == -50  # currently passes


# ---------------- COUPON TESTS ----------------
def test_apply_coupon_valid():
    assert apply_coupon(100, "SAVE10") == 90


# ❌ FAILS (case sensitivity bug)
# def test_apply_coupon_case_issue():
#     assert apply_coupon(100, "SAVE20") == 80


# ---------------- SHIPPING TESTS ----------------
# ❌ FAILS (wrong formula)
# def test_calculate_shipping():
#     assert calculate_shipping(10, 20) == 200


# ---------------- TAX SLAB TESTS ----------------
def test_tax_slab_high():
    assert apply_tax_slabs(1200) == 216


# ⚠️ Might pass or fail depending on bug
def test_tax_slab_mid():
    assert apply_tax_slabs(600) == 108  # matches current buggy logic


# ---------------- FINAL BILL ----------------
# ❌ FAILS (wrong order of operations)
# def test_final_bill():
#     result = final_bill(100, 0.1, 10, "SAVE10")
#     assert result == 81
