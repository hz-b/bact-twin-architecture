from ..data_model.conversion_info import CurvePoint
from ..interfaces.state_conversion import StateConversion
import logging
from typing import Sequence, Tuple
from scipy.interpolate import interp1d
import numpy as np


logger = logging.getLogger("bact-twin-architecture")


class UnitConversion(StateConversion):
    """a one dimensional conversion"""


class LinearUnitConversion(UnitConversion):
    """uses linear polynom.

    Warning:
        inverse will fail for slopes of 0
    """

    def __init__(self, *, intercept: float, slope: float):
        self.intercept = intercept
        self.slope = slope

    def forward(self, state: float) -> float:
        return self.intercept + self.slope * state

    def inverse(self, state: float) -> float:
        return (state - self.intercept) / self.slope


class EnergyIndependentLinearUnitConversion(StateConversion):
    """Typical example: magnet parameters

    Todo:
        Handle separately if brho changes
    """
    def __init__(self, *, intercept: float, slope: float, brho: float):
        self.intercept = intercept
        self.slope = slope
        self.brho = brho

    def forward(self, state: float) -> float:
        logger.info("%s.forward: brho %s, intercept %s slope %s, state %s", self.__class__.__name__, self.brho, self.intercept, self.slope, state)
        intercept = self.intercept * self.brho
        slope = self.slope * self.brho
        return intercept + slope * state

    def inverse(self, state: float) -> float:
        logger.info("%s.inverse: brho %s, intercept %s slope %s, state %s", self.__class__.__name__, self.brho, self.intercept, self.slope, state)
        intercept = self.intercept * self.brho
        slope = self.slope * self.brho
        return (state - intercept) / slope


class EnergyIndependentCurveUnitConversion(UnitConversion):
    """
    Interpolate a curve (independent -> dependent) using scipy.interpolate.interp1d
    and scale by `brho`.

    - points: sequence of 2-tuples (indep, dep) or objects with `indep` and `dep`.
    - forward(x) -> interpolated_dep(x) * brho
    - inverse(y) -> x such that interpolated_dep(x) == y / brho (searches segments;
      works for non-monotonic curves by returning the first matching segment)
    """

    def __init__(self, *, fwd_points: Sequence[CurvePoint], bwd_points: Sequence[CurvePoint], brho: float):
        # forward interpolator: will raise if x out of bounds
        self._fwd = interp1d(
            [t["indep"] for t in fwd_points],
            [t["dep"] for t in fwd_points],
            kind="linear", bounds_error=True, assume_sorted=True)
        self._bwd = interp1d(
            [t["indep"] for t in bwd_points],
            [t["dep"] for t in bwd_points],
            kind="linear", bounds_error=True, assume_sorted=True)
        self.brho = float(brho)

    def forward(self, state: float) -> float:
        logger.info("%s.forward: brho %s points %d state %s", self.__class__.__name__, self.brho, len(self._indep), state)
        x = float(state)
        y = float(self._fwd(x))  # interp1d returns an array-like
        return y * self.brho

    def inverse(self, state: float) -> float:
        logger.info("%s.inverse: brho %s points %d state %s", self.__class__.__name__, self.brho, len(self._indep), state)
        if self.brho == 0:
            raise ValueError("brho must be non-zero for inversion")
        target = float(state) / self.brho
        y = float(self._bwd(target))  # interp1d returns an array-like
        return y

