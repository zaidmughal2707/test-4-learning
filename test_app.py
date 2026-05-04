from app import add_numbers

def test_addition():
    # To FAIL: change 15 to 20
    # To PASS: keep it at 15
    assert add_numbers(10, 5) == 20
