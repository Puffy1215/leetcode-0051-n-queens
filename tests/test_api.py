"""Tests API for solving problem N-Queens"""

import pytest

from leetcode_0051_n_queens import api


@pytest.mark.parametrize(
    ["result", ...],
    (
        [..., ...],
        [..., ...],
    )
)
def test_n_queens(result, ...) -> None:
    """Tests solution for problem N-Queens"""

    assert api.n_queens(...) == result