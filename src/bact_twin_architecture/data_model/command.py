from dataclasses import dataclass
from enum import IntEnum
from typing import Sequence, Union

# from ..interfaces.identifier import LatticeElementIdentifier, DeviceIdentifier


class BehaviourOnError(IntEnum):
    stop = 1
    ignore = 2
    roll_back = 3


@dataclass
class Command:
    """
    Todo:
        consider if the id should just be a string
        use documentation to make clear what it is
    """
    #: can be the identifer of a lattice element or a device
    id: str
    property: str
    value: object
    behaviour_on_error: BehaviourOnError


@dataclass
class CommandSequence:
    commands: Sequence[Command]


__all__ = ["BehaviourOnError", "Command", "CommandSequence"]
