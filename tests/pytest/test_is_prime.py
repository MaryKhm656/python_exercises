from is_prime import is_prime

def test_is_prime():
    assert is_prime(-5) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(5) == True
    assert is_prime(4) == False
    assert is_prime(9) == False