import pytest
from .expense_report import prod_of_2020_sum

@pytest.mark.parametrize(
    "expenses,expected",
    [
        (
            [1721, 979, 366, 299, 675, 1456], 514579
        ),
        (
            [2000, 20], 40000
        )
    ]
)
def test_prod_of_2020_sum(expenses, expected):
    assert expected == prod_of_2020_sum(expenses)

def test_prod_of_2020_sum_raises_error_when_no_2020_sum_present():
    with pytest.raises(AttributeError):
        prod_of_2020_sum([1, 2, 3])


