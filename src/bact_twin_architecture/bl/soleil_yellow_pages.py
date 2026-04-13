from enum import Enum
from typing import Sequence, Union, Any

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
        if isinstance(family_name, FamilyName):
            key = family_name.value
        else:
            key = str(family_name)
        return self._d[key]

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


def soleil_yellow_pages(
    elements: list[dict[str, Any]] | None = None,
) -> YellowPages:
    """
    Creates a YellowPages instance for SOLEIL using the magnet names
    from ~/Documents/soleil/accelerator_setup.json.
    """

    if elements is None:
        raise RuntimeError(
            "Accelerator setup is not loaded. "
            "Provide `elements` explicitly or initialize accelerator_config first."
        )
    def is_horizontal(e: dict) -> bool:
        name = e["name"]
        fam = e.get("FamName", "")
        return "CDLH" in name or fam.endswith("_HCOR")

    def is_vertical(e: dict) -> bool:
        name = e["name"]
        fam = e.get("FamName", "")
        return "CDLV" in name or fam.endswith("_VCOR")

    quadrupoles = [e["name"] for e in elements if e["type"] == "Quadrupole"]
    sextupoles = [e["name"] for e in elements if e["type"] == "Sextupole"]
    bends = [e["name"] for e in elements if e["type"] == "Bend"]
    multipoles = [e["name"] for e in elements if e["type"] == "Multipole"]

    # All steerers are `type == "Steerer"`, split by name/FamName
    horizontal_steerers = [
        e["name"] for e in elements
        if e["type"] == "Steerer" and is_horizontal(e)
    ]
    vertical_steerers = [
        e["name"] for e in elements
        if e["type"] == "Steerer" and is_vertical(e)
    ]

    d = dict(
        quadrupoles=quadrupoles,
        sextupoles=sextupoles,
        bends=bends,
        multipoles=multipoles,
        horizontal_steerers=horizontal_steerers,
        vertical_steerers=vertical_steerers,
    )

    return YellowPages(d)
