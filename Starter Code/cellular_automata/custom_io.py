from datatypes import GameBoard

def read_board_from_file(filename: str) -> GameBoard:
    """
    Read a CSV of integers into a GameBoard (2D list[int]).
    """
    if not isinstance(filename, str) or len(filename) == 0:
        raise ValueError("filename must be a non-empty string.")
    board: GameBoard = []
    with open(filename, "r", encoding="utf-8") as f:
        # strip trailing/leading whitespace, split into lines
        lines = f.read().strip().splitlines()
    for line in lines:
        elements = line.split(",")
        board.append(set_row_values(elements))
    return board

def set_row_values(line_elements: list[str]) -> list[int]:
    """
    Convert a list of numeric strings into a row of ints.
    """
    if not isinstance(line_elements, list) or len(line_elements) == 0:
        raise ValueError("line_elements must be a non-empty list of strings.")
    row: list[int] = []
    for s in line_elements:
        s_stripped = s.strip()
        try:
            row.append(int(s_stripped))
        except ValueError as e:
            raise ValueError(f"Invalid integer '{s}' in board file.") from e
    return row

def read_rules_from_file(filename: str) -> dict[str, int]:
    """
    Read rules from a text file where each line looks like: <neighborhood>:<next_state>

    Returns:
        dict[str, int]: mapping neighborhood-string -> next-state int
    """
    if not isinstance(filename, str) or len(filename) == 0:
        raise ValueError("filename must be a non-empty string.")
    # TODO: implement parsing of rules file
    return {}