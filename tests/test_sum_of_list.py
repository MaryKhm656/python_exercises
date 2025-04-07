from sum_of_list import sum_of_list

def test_sum():
    assert sum_of_list([1, 2, 3]) == 6
    assert sum_of_list([-1, -2, -3]) == -6
    assert sum_of_list([0, 0, 0]) == 0
    assert sum_of_list([]) == 0