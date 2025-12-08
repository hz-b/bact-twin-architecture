from enum import Enum
from typing import Sequence, Union

from ..interfaces.family_tree import FamilyTree


class FamilyName(Enum):
    quadrupoles = "quadrupoles"
    sextupoles = "sextupoles"
    horizontal_steerers = "horizontal_steerers"
    vertical_steerers = "vertical_steerers"


class YellowPages(FamilyTree):
    """

    Todo:
        review if separate methods should be used for
        * horizontal_steerer_names
        * vertical_steerer_names

        or use:
        get(family_name: str)
    """

    def __init__(self, d: dict):
        self._d = d

    def get(self, family_name: Union[str, FamilyName]) -> Sequence[str]:
        # check for valid key?
        # key = str(FamilyName(family_name))
        return self._d[family_name]

    def horizontal_steerer_names(self) -> Sequence[str]:
        return self.get("horizontal_steerers")

    def vertical_steerer_names(self) -> Sequence[str]:
        return self.get("vertical_steerers")

    def quadrupole_names(self) -> Sequence[str]:
        return self.get("quadrupoles")

    def sextupole_names(self) -> Sequence[str]:
        return self.get("sextupoles")


def soleil_yellow_pages(elements: list[dict]) -> YellowPages:
    """
    Create a SOLEIL YellowPages instance using the accelerator data.

    Parameters
    ----------
    elements : list[dict]
        Parsed SOLEIL database entries. Each entry must contain:
        - "type": str  (e.g., "Quadrupole", "Sextupole")
        - "name": str

    Returns
    -------
    YellowPages
        An instance with families:
            * quadrupoles
            * sextupoles
            * bends
            * multipoles
    """

    # Collect magnet names by type
    quadrupoles = [el["name"] for el in elements if el["type"] == "Quadrupole"]
    sextupoles = [el["name"] for el in elements if el["type"] == "Sextupole"]
    bends = [el["name"] for el in elements if el["type"] == "Bend"]
    multipoles = [el["name"] for el in elements if el["type"] == "Multipole"]

    d = dict(
        quadrupoles=quadrupoles,
        sextupoles=sextupoles,
        bends=bends,
        multipoles=multipoles,
    )

    return YellowPages(d)
