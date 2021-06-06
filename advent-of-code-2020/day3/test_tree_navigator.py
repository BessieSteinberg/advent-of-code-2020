import pytest
from .tree_navigator import count_trees_hit

TEST_DATA = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


@pytest.mark.parametrize(
    "x_delta,expected",
    [
        (3, 7),
        (0, 3)
    ]
)
def test_count_trees_hit(x_delta, expected):
    assert expected == count_trees_hit(TEST_DATA, x_delta)
