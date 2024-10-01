from dataclasses import dataclass
from enum import IntEnum

from ..interfaces.identifier import Identifier


class BehaviourOnError(IntEnum):
    stop = 1
    ignore = 2
    roll_back = 3

@dataclass
class Command:
    id: Identifier
    property: str
    value : object
    behaviour_on_error : BehaviourOnError
    