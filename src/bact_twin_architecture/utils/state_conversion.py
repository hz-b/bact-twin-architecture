"""Handle 1-to-m m-to-1 or similar ones

Todo:
    use unit conversion interface if provided
"""
import logging
from typing import Dict, Sequence

from .unit_conversion import UnitConversion
from ..interfaces.state_conversion import StateConversion

logger = logging.getLogger("bact-twin-architecture")


class ConversionManyToOne(StateConversion):
    """Tailored to a combined functions magnet with only one current

    Currently assuming that forward is from a single value to a single
    value. The

    Can be further generalised
    """
    def __init__(
        self,
        *,
        unit_conversions: Dict[str: UnitConversion],
        forward_positive_list: Sequence[str],
    ):
        self.unit_conversions =  unit_conversions
        self.forward_positive_list = forward_positive_list

    def forward(self, identifer: str, value: float) -> float:
        """

        Todo:
            review interface definition of state conversion
        """
        if identifer not in self.forward_positive_list:
            raise AssertionError(f"refusing forward conversion: {identifer=} not in {self.forward_positive_list}")

        return self.unit_conversions.get(identifer).forward(value)

    def inverse(self, value: float) -> Dict[str, float]:
        return {identifier: interp.inverse(value) for identifier, interp in self.unit_conversions}