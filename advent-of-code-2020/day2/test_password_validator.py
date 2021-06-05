import pytest
from .password_validator import count_valid_passwords, is_password_valid


@pytest.mark.parametrize(
    "policy_password_list,expected_valid",
    [
        (
            [
                "1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc",
            ],
            2
        ),
        (
            [
                "18-20 y: bessie",
                "2-10 e: bessie"
            ],
            1
        )
    ]
)
def test_count_valid_passwords(policy_password_list, expected_valid):
    assert expected_valid == count_valid_passwords(policy_password_list)


@pytest.mark.parametrize(
    "s,expected",
    [
        ("1-3 a: abcde", True),
        ("1-3 b: cdefg", False),
        ("2-9 c: ccccccccc", True),
        ("18-20 y: bessie", False),
        ("2-10 e: bessie", True)
    ]
)
def test_is_password_valid(s, expected):
    assert expected == is_password_valid(s)
