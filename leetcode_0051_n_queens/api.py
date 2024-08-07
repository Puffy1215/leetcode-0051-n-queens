"""API for solving problem N-Queens"""

from copy import deepcopy
from typing import Iterator

N_MAX = 9
N_MIN = 1


def _check_preconditions(n: int) -> bool:
    return N_MIN <= n <= N_MAX


GOOD = " "
BAD = "."
QUEEN = "Q"


def _set_bad(board: list[list[str]], x: int, y: int) -> None:
    if board[y][x] != QUEEN:
        board[y][x] = BAD


def _set_queen(board: list[list[str]], x: int, y: int) -> None:
    n = len(board)
    assert 0 <= x < n
    assert 0 <= y < n
    assert board[y][x] == GOOD

    board[y][x] = QUEEN

    for i in range(1, n):
        if y + i < n:
            _set_bad(board, x, y + i)
        if y - i >= 0:
            _set_bad(board, x, y - i)
        if x + i < n:
            _set_bad(board, x + i, y)
            if y + i < n:
                _set_bad(board, x + i, y + i)
            if y - i >= 0:
                _set_bad(board, x + i, y - i)
        if x - i >= 0:
            _set_bad(board, x - i, y)
            if y + i < n:
                _set_bad(board, x - i, y + i)
            if y - i >= 0:
                _set_bad(board, x - i, y - i)


def _recursive_n_queens(board: list[list[str]], y: int) -> Iterator[list[list[str]]]:
    n = len(board)

    for x in range(n):
        if board[y][x] == GOOD:
            copy = deepcopy(board)
            _set_queen(copy, x, y)
            if y == n - 1:
                yield copy
            else:
                for b in _recursive_n_queens(copy, y + 1):
                    yield b


def n_queens(n: int) -> Iterator[list[list[str]]]:
    """Solves problem N-Queens"""

    assert _check_preconditions(n)

    board = [[GOOD] * n for _ in range(n)]

    for b in _recursive_n_queens(board, 0):
        yield b
