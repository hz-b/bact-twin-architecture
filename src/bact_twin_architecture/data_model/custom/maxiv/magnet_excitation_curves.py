from dataclasses import dataclass
from typing import Sequence

from ...conversion_info import CurvePoint
from ...harmonic_id import Harmonic
from ...location import SectorCellBasedLocationName


@dataclass
class MaxIVR1ExcitationMetaData:
    trl: str
    loc: SectorCellBasedLocationName


@dataclass
class MaxIVR1ExcitationDataImport:
    harmonic : Harmonic
    md: MaxIVR1ExcitationMetaData
    curve: Sequence[CurvePoint]


@dataclass
class MaxIVR1ExcitationDataSingleCurve:
    harmonic: Harmonic
    curve: Sequence[CurvePoint]


@dataclass
class MaxIVExcitationData:
    md: MaxIVR1ExcitationMetaData
    curves: Sequence[MaxIVR1ExcitationDataSingleCurve]
