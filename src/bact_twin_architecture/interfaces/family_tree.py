"""Info on which device belongs to which other
"""
from abc import abstractmethod, ABCMeta
from typing import Sequence


class FamilyTree(metaclass=ABCMeta):
    """Handling lattice element and their family belonging

    Todo:
        Shall one distinquish that ?

    Two ways to see it:
    * family as seen by a lattice:
        typically some magnets that are split all over the place

    Imagine for some lattice e.g. some quadrupoles could be
    indentically as they are produced. But they could still
    belong to different families
    """
    @abstractmethod
    def get(self, family_name: str) -> Sequence[str]:
        """Return a sequence with all identifiers beloning to base class"""
        raise NotImplementedError("use derived class instead")