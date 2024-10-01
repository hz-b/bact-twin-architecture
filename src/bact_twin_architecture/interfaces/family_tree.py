"""Info on which device belongs to which other
"""
from abc import abstractmethod, ABCMeta
from typing import Sequence

from .identifier import Identifier


class FamilyTree(metaclass=ABCMeta):
    """
    Waring:
        need to change the name. Yellow Pages
        is a trademark...
    """
    @abstractmethod
    def get(self, family_name: str) -> Sequence[Identifier]:
        """Return a sequence with all identifiers beloning to base class"""
        raise NotImplementedError("use derived class instead")