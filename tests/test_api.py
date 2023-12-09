"""Tests API for solving problem N-Queens"""

import pytest

from leetcode_0051_n_queens import api


@pytest.mark.parametrize(
    ["result", "n"],
    (
        [[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]], 4],
        [[["Q"]], 1],
    ),
)
def test_n_queens(result: list[list[str]], n: int) -> None:
    """Tests solution for problem N-Queens"""

    assert api.n_queens(n) == result
