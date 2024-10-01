from dataclasses import dataclass
from enum import IntEnum
from typing import Sequence

from ..interfaces.identifier import Identifier


class BehaviourOnError(IntEnum):
    stop = 1
    ignore = 2
    roll_back = 3


@dataclass
class Command:
    id: Identifier
    property: str
    value: object
    behaviour_on_error: BehaviourOnError


@dataclass
class CommandSequence:
    commands: Sequence[Command]


__all__ = ["BehaviourOnError", "Command", "CommandSequence"]
