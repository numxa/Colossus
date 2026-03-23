
from dataclasses import dataclass
from enum import Enum
from typing import Optional

NUMBER_OF_ROUNDS = 3


class Team(Enum):
    BLUE = "blue"
    RED = "red"
    NEITHER = "neither"


SCENARIO_INITIATIVES = {
    1: Team.RED,
    2: None,
    3: None
}


@dataclass
class RoundState:
    round: int
    initiative: Optional[Team]
