import json
from enum import Enum
from pathlib import Path
from typing import Sequence, Union

from ..interfaces.family_tree import FamilyTree


class FamilyName(Enum):
    quadrupoles = "quadrupoles"
    sextupoles = "sextupoles"
    bends = "bends"
    multipoles = "multipoles"
    horizontal_steerers = "horizontal_steerers"
    vertical_steerers = "vertical_steerers"


class YellowPages(FamilyTree):
    def __init__(self, d: dict):
        self._d = d

    def get(self, family_name: Union[str, FamilyName]) -> Sequence[str]:
        return self._d[family_name]

    def quadrupole_names(self) -> Sequence[str]:
        return self.get("quadrupoles")

    def sextupole_names(self) -> Sequence[str]:
        return self.get("sextupoles")

    def bend_names(self) -> Sequence[str]:
        return self.get("bends")

    def multipole_names(self) -> Sequence[str]:
        return self.get("multipoles")

    def horizontal_steerer_names(self) -> Sequence[str]:
        return self.get("horizontal_steerers")

    def vertical_steerer_names(self) -> Sequence[str]:
        return self.get("vertical_steerers")


def soleil_yellow_pages() -> YellowPages:
    """
    Creates a YellowPages instance for SOLEIL using the magnet names
    from ~/Documents/soleil/accelerator_setup.json.
    """

    # Path to the SOLEIL accelerator setup file
    data_file = Path.home() / "Documents" / "soleil" / "accelerator_setup.json"

    elements = json.loads(data_file.read_text())

    quadrupoles = [e["name"] for e in elements if e["type"] == "Quadrupole"]
    sextupoles = [e["name"] for e in elements if e["type"] == "Sextupole"]
    bends = [e["name"] for e in elements if e["type"] == "Bend"]
    multipoles = [e["name"] for e in elements if e["type"] == "Multipole"]
    horizontal_steerers = [e["name"] for e in elements if e["type"] == "None"]
    vertical_steerers = [e["name"] for e in elements if e["type"] == "None"]

    d = dict(
        quadrupoles=quadrupoles,
        sextupoles=sextupoles,
        bends=bends,
        multipoles=multipoles,
        horizontal_steerers=horizontal_steerers,
        vertical_steerers=vertical_steerers,
    )

    return YellowPages(d)
