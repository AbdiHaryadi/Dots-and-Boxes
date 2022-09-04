from typing import NamedTuple, Literal, Tuple

class GameAction(NamedTuple):
    """
    action_type: "row" or "col"
    position: (x: int, y: int)

    If action_type == "row", a horizontal line will be marked.
    Vertical for otherwise.

    Position starts from (0, 0).
    """

    action_type: Literal["row", "col"]
    position: Tuple[int, int]
