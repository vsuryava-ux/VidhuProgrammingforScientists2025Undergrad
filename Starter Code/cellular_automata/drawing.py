from datatypes import GameBoard
from functions import assert_rectangular
import pygame


def draw_game_board(board: GameBoard, cell_width: int):
    """
    Draw a single GameBoard to an image/surface (implementation up to you).
    Returns an image-like object (e.g., a PIL.Image, a pygame.Surface, etc.).
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty 2D list.")
    assert_rectangular(board)
    if not isinstance(cell_width, int) or cell_width <= 0:
        raise ValueError("cell_width must be a positive integer.")

    # TODO: implement drawing logic
    return None

def draw_game_boards(boards: list[GameBoard], cell_width: int) -> list:
    """
    Draw multiple GameBoards and return a list of images/surfaces.
    """
    if not isinstance(boards, list) or len(boards) == 0:
        raise ValueError("boards must be a non-empty list of GameBoard objects.")
    if not isinstance(cell_width, int) or cell_width <= 0:
        raise ValueError("cell_width must be a positive integer.")

    # TODO: implement multiple-board drawing
    return []