from abc import ABCMeta, abstractmethod
from typing import Tuple
from .identifier import LatticeElementIdentifier, DeviceIdentifier


class IdentifierPropertyTransformerBase(metaclass=ABCMeta):
    """transforms pairs of (id, property)
    """

    @abstractmethod
    def forward(self, id_: LatticeElementIdentifier, property: str) -> Tuple[DeviceIdentifier, str]:
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def inverse(self, id_: DeviceIdentifier, property: str) -> Tuple[LatticeElementIdentifier, str]:
        raise NotImplementedError("use derived class instead")

