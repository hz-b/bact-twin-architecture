from ..data_model.conversion_info import CurvePoint
from ..interfaces.state_conversion import StateConversion
import logging
from typing import Sequence
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
        logger.info(
            "%s.forward: brho %s, intercept %s slope %s, state %s",
            self.__class__.__name__,
            self.brho,
            self.intercept,
            self.slope,
            state,
        )
        intercept = self.intercept * self.brho
        slope = self.slope * self.brho
        return intercept + slope * state

    def inverse(self, state: float) -> float:
        logger.info(
            "%s.inverse: brho %s, intercept %s slope %s, state %s",
            self.__class__.__name__,
            self.brho,
            self.intercept,
            self.slope,
            state,
        )
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

    def __init__(
        self,
        *,
        fwd_points: Sequence[CurvePoint],
        bwd_points: Sequence[CurvePoint],
        brho: float,
        # todo: see how it was named at max iv
        #       iimplement it in a filter delegating implementation to this object
        flip_dep_sign: False
    ):
        # forward interpolator: will raise if x out of bounds
        # TODO: clean up it is a mess at the moment
        self._fwd = interp1d(
            [t.indep for t in fwd_points],
            [t.dep for t in fwd_points],
            kind="linear",
            # Todo: change later to true ... or make user configurable
            bounds_error=False,
        )
        self._bwd = interp1d(
            [t.indep for t in bwd_points],
            [t.dep for t in bwd_points],
            kind="linear",
            # Todo: change later to true ... or make user configurable
            bounds_error=False,
        )
        self.brho = float(brho)
        self.fwd_points = fwd_points
        self.bwd_points = bwd_points
        self.flip_dep_sign = flip_dep_sign

    def forward(self, state: float) -> float:
        logger.info(
            "%s.forward: brho %s state %s", self.__class__.__name__, self.brho, state
        )
        x = float(state)
        y = float(self._fwd(x))  # interp1d returns an array-like
        if self.flip_dep_sign:
            y = -y
        return  y * self.brho

    def inverse(self, state: float) -> float:
        # logger.info("%s.inverse: brho %s points %d state %s", self.__class__.__name__, self.brho, len(self._indep), state)
        if self.brho == 0:
            raise ValueError("brho must be non-zero for inversion")
        if self.flip_dep_sign:
            nstate = -state
        else:
            nstate = state
        target = float(nstate) / self.brho
        y = float(self._bwd(target)) # interp1d returns an array-like
        assert np.isfinite(y), "failed to inverse {state=} ({brho=}, {target=})"
        return y
