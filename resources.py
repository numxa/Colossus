
from dataclasses import dataclass
from enum import Enum
from typing import Optional

NUMBER_OF_ROUNDS = 3
REQUIRED_VP_FOR_INITIATIVE = 5


class InitiativeStatus(Enum):
    BLUE = "blue"
    RED = "red"
    CONTESTED = "contested"


SCENARIO_INITIATIVES = {
    1: InitiativeStatus.RED,
    2: None,
    3: None
}


@dataclass
class RoundState:
    round: int
    initiative: Optional[InitiativeStatus]
    prev_initiative: Optional[InitiativeStatus]
    vp_blue: int
    prev_vp_blue: int
    vp_red: int
    prev_vp_red: int