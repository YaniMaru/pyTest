import pytest
from methods import *


@pytest.mark.parametrize('a, expected_result', [(5, 11.55),
                                                (6, 14.07)])
def test_methods(a, expected_result):
    assert get_list(a) == expected_result


@ pytest.mark.parametrize('list1, expected_result', [([2, 3, 4, 5, 6], [12, 15, 16]),
                                                     ([2, 3, 5, 6], [12, 15])])
def test_multiply_pair_num(list1, expected_result):
    assert multiply_pair_num(list1) == expected_result


@pytest.mark.parametrize('num, expected_result', [(45, str(101101)),
                                                  (3, str(11))])
def test_binary(num, expected_result):
    assert binary(num) == expected_result


@pytest.mark.parametrize('list1, expected_result', [([2, 3, 5, 9, 3], 12),
                                                    ([1, 4, 7, 9, 8], 13)])
def test_sum_of_odd(list1, expected_result):
    assert sum_of_odd(list1) == expected_result


@pytest.mark.parametrize('num, expected_result', [(4, [-3, 2, -1, 1, 0, 1, 1, 2, 3]),
                                                  (2, [-1, 1, 0, 1, 1]),
                                                  (3, [2, -1, 1, 0, 1, 1, 2])])
def test_fibonacci(num, expected_result):
    assert fibonacci(num) == expected_result
