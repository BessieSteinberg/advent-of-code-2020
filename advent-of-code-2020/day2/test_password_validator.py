import pytest
from .password_validator import count_valid_passwords_policy_1, is_password_valid, count_valid_passwords_policy_2


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
                "2-10 e: bessie",
                "1-6 s: bessie"
            ],
            2
        )
    ]
)
def test_count_valid_passwords_policy_1(policy_password_list, expected_valid):
    assert expected_valid == count_valid_passwords_policy_1(policy_password_list)


@pytest.mark.parametrize(
    "policy_password_list,expected_valid",
    [
        (
            [
                "1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc",
            ],
            1
        ),
        (
            [
                "18-20 y: bessie",
                "2-10 e: bessie",
                "1-6 s: bessie"
            ],
            1
        )
    ]
)
def test_count_valid_passwords_policy_2(policy_password_list, expected_valid):
    assert expected_valid == count_valid_passwords_policy_2(policy_password_list)


@pytest.mark.parametrize(
    "s,policy,expected",
    [
        ("1-3 a: abcde", 1, True),
        ("1-3 b: cdefg", 1, False),
        ("2-9 c: ccccccccc", 1, True),
        ("18-20 y: bessie", 1, False),
        ("2-10 e: bessie", 1, True),
        ("1-6 s: bessie", 1, True),
        ("1-3 a: abcde", 2, True),
        ("1-3 b: cdefg", 2, False),
        ("2-9 c: ccccccccc", 2, False),
        ("18-20 y: bessie", 2, False),
        ("2-6 e: bessie", 2, False),
        ("1-6 s: bessie", 2, False),
    ]
)
def test_is_password_valid(s, policy, expected):
    assert expected == is_password_valid(s, policy)

# TODO: add invalid policy test
