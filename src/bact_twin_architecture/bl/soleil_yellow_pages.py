from enum import Enum
from typing import Sequence, Union
import json
from pathlib import Path

from ..interfaces.family_tree import FamilyTree


class FamilyName(Enum):
    quadrupoles = "quadrupoles"
    sextupoles = "sextupoles"
    bends = "bends"
    multipoles = "multipoles"


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


def soleil_yellow_pages() -> YellowPages:
    """
    Creates a YellowPages instance for SOLEIL using the magnet names
    from ~/Documents/soleil/accelerator_setup.json.
    """

    # Path to the SOLEIL accelerator setup file
    data_file = Path.home() / "Documents" / "soleil" / "accelerator_setup.json"

    elements = json.loads(data_file.read_text())

    quadrupoles = [e["name"] for e in elements if e["type"] == "Quadrupole"]
    sextupoles  = [e["name"] for e in elements if e["type"] == "Sextupole"]
    bends       = [e["name"] for e in elements if e["type"] == "Bend"]
    multipoles  = [e["name"] for e in elements if e["type"] == "Multipole"]

    d = dict(
        quadrupoles=quadrupoles,
        sextupoles=sextupoles,
        bends=bends,
        multipoles=multipoles,
    )

    return YellowPages(d)
