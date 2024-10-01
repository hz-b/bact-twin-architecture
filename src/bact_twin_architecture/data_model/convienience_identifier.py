"""Not used yet

Todo:
    Review identifiers! Are the following identifiers the same

    * place location identifer
    * lattice element identifer
    * device identifer
    * module identifier: e.g. nested magnets
    * assembly identifer: e.g. magnets on a grider

    If identifers are unique any inconsistent use would be traced

"""
from dataclasses import dataclass


@dataclass(eq=True)
class StandardIdentifier:
    """
    Todo: Is that the standard approach for MML?
    """

    # name: str
    family_name: str
    sector: int
    child_number: int
