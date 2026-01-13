from dataclasses import dataclass
from typing import Literal


@dataclass
class Harmonic:
    number: int
    type: Literal["normal", "skew", "unknown"]