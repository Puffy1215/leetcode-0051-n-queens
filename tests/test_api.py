"""Tests API for solving problem N-Queens"""

import pytest

from leetcode_0051_n_queens import api


def _to_list(board: str) -> list[list[str]]:
    rows = board.split("\n")
    rows = [r.strip() for r in rows]
    rows = [r for r in rows if r]
    return [list(r) for r in rows]


_BOARDS_4 = [
    """
    .Q..
    ...Q
    Q...
    ..Q.
    """,
    """
    ..Q.
    Q...
    ...Q
    .Q..
    """,
]

_BOARDS_1 = [
    """
    Q
    """,
]


@pytest.mark.parametrize(
    ["result", "n"],
    (
        [[_to_list(b) for b in _BOARDS_4], 4],
        [[], 3],
        [[], 2],
        [[_to_list(b) for b in _BOARDS_1], 1],
    ),
)
def test_n_queens(result: list[list[list[str]]], n: int) -> None:
    """Tests solution for problem N-Queens"""

    assert list(api.n_queens(n)) == result


@pytest.mark.parametrize(
    ["result", "n"],
    (
        [10, 5],
        [4, 6],
        [40, 7],
        [92, 8],
        [352, 9],
    ),
)
def test_n_queens_count(result: int, n: int) -> None:
    """Tests solution for problem N-Queens"""

    assert len(list(api.n_queens(n))) == result
