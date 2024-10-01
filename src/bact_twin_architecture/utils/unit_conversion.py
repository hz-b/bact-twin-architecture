from ..interfaces.state_conversion import StateConversion

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

