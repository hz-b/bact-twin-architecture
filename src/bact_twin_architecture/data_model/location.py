from dataclasses import dataclass


@dataclass
class SectorCellBasedLocationName:
    sector: int
    cell: int
    subcell: int

