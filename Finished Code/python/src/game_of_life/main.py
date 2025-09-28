import sys
import pygame
import numpy
import imageio
from custom_io import read_board_from_file
from functions import play_game_of_life
from drawing import draw_game_board, draw_game_boards


def pygame_surface_to_numpy(surface: pygame.Surface) -> numpy.ndarray:
    """
    Convert a Pygame Surface to a NumPy RGB image array.
    Returns:
        numpy.ndarray: Frame as (height, width, 3) array.
    """
    return None  # TODO: implement


def main():
    print("Coding the Game of Life!")

    # initialize pygame 
    pygame.init()

    # read the board from file 
    r_pentomino = read_board_from_file("boards/rPentomino.csv")

    cell_width = 20

    surface = draw_game_board(r_pentomino, cell_width)

    print("We made the surface?")

    print("We don't really know because we need to visualize the surface.")

    pygame.quit()

    """
    if len(sys.argv) != 5:
        raise ValueError("Usage: python main.py initial_board.csv output_prefix cell_width num_gens")

    input_csv = sys.argv[1]
    output_prefix = sys.argv[2]
    cell_width = int(sys.argv[3])
    num_gens = int(sys.argv[4])

    print("Parameters read in successfully!")
    # TODO: implement simulation, drawing, video writing
    """


if __name__ == "__main__":
    main()
