"""

Todo:
    should be moved to an implementation part
"""

from dataclasses import dataclass
from .identifiers import ConversionID


@dataclass(frozen=True)
class LinearUnitConversionInfo:
    """
    """
    conversion_id : ConversionID
    intercept: float
    slope: float
