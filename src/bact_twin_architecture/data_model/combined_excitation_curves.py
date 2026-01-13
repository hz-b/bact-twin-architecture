from dataclasses import dataclass
from typing import Sequence

from .conversion_info import CurvePoint
from .harmonic_id import Harmonic


@dataclass
class ExcitationDataSingleCurve:
    harmonic: Harmonic
    curve: Sequence[CurvePoint]


@dataclass
class ExcitationDataCollection:
    curves: Sequence[ExcitationDataSingleCurve]