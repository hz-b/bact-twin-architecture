"""Handle 1-to-m m-to-1 or similar ones

Todo:
    use unit conversion interface if provided
"""
import logging
from typing import Dict, Sequence

from .unit_conversion import UnitConversion
from ..interfaces.state_conversion import StateConversion

logger = logging.getLogger("bact-twin-architecture")


class ConversionManyToOne:
    """Tailored to a combined functions magnet with only one current

    Currently assuming that forward is from a single value to a single
    value. The

    Can be further generalised
    """

    def __init__(
        self,
        *,
        unit_conversions: Dict[str, UnitConversion],
        forward_positive_list: Sequence[str],
    ):
        self.unit_conversions = unit_conversions
        self.forward_positive_list = forward_positive_list

    def forward(self, identifier: str, value: float) -> float:
        """

        Todo:
            review interface definition of state conversion
        """
        if identifier not in self.forward_positive_list:
            raise AssertionError(
                f"refusing forward conversion: {identifier=} not in {self.forward_positive_list}"
            )

        return self.unit_conversions.get(identifier).forward(value)

    def inverse(self, value: float) -> Dict[str, float]:
        return {
            identifier: interp.inverse(value)
            for identifier, interp in self.unit_conversions.items()
        }


class ConversionManyToOneProxy(StateConversion):
    """
    Todo:
        see if identifier is a good name

    It is the identifier that will changes *all associated values* if
    an update request is made. The change will not happen here, but any
    call to inverse will then request that all values are updated
    """

    def __init__(self, *, proxy_to: ConversionManyToOne, identifier: str):
        self.proxy_to = proxy_to
        self.identifer = identifier

    def forward(self, value: float) -> float:
        return self.proxy_to.forward(self.identifer, value)

    def inverse(self, value: float) -> Dict[str, float]:
        return self.proxy_to.inverse(value)
