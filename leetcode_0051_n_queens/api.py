"""API for solving problem N-Queens"""

from typing import Iterator

N_MAX = 9
N_MIN = 1


def _check_preconditions(n: int) -> bool:
    return N_MIN <= n <= N_MAX


def _recursive_n_queens(board: list[str]) -> Iterator[list[str]]:
    pass


def n_queens(n: int) -> Iterator[list[str]]:
    """Solves problem N-Queens"""

    assert _check_preconditions(n)

    board = ["." * n] * n
    for i in range(n):
        pass
