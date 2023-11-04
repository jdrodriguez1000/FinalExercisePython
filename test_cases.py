import pytest
from arithmetics import myAddition


@pytest.fixture
def var_test():
    return myAddition()


def test_add_two_numbers_minimum_ok(var_test):
    assert var_test.add_two_numbers(2,3)==5

@pytest.mark.parametrize(
    ['input_1', 'input_2', 'output_1'],
    [
        (2,4,6),
        (4,2,6),
        (-1,2,1),
        (2,-1,1),
        (0,3,3),
        (3,0,3)
    ]
)
def test_add_two_numbers_multiple_ok(var_test, input_1, input_2, output_1):
    assert var_test.add_two_numbers(input_1, input_2) == output_1   
    
def test_add_two_numbers_minimum_fail(var_test):
    expected = 'Data types not correct'
    assert var_test.add_two_numbers('e',3) == expected
    
@pytest.mark.parametrize(
    ['input_1', 'input_2'],
    [
        ('q',2),
        (4, 'ff'),
        ('', 4),
        (6, '')
    ]
)
def test_add_two_numbers_string(var_test, input_1, input_2):
    expected = 'Data types not correct'
    assert var_test.add_two_numbers(input_1, input_2) == expected
    