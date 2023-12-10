"""API for solving problem N-Queens"""

from typing import Iterator

N_MAX = 9
N_MIN = 1


def _check_preconditions(n: int) -> bool:
    return N_MIN <= n <= N_MAX


def n_queens(n: int) -> Iterator[list[list[str]]]:
    """Solves problem N-Queens"""

    assert _check_preconditions(n)

    pass
