from abc import ABCMeta, abstractmethod
from typing import Tuple
from ..data_model.identifiers import LatticeElementPropertyID, DevicePropertyID


class IdentifierPropertyTransformerBase(metaclass=ABCMeta):
    """transforms pairs of (id, property)
    """
    @abstractmethod
    def forward(self, id_: LatticeElementPropertyID) -> DevicePropertyID:
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def inverse(self, id_: DevicePropertyID) -> Tuple[LatticeElementPropertyID, str]:
        raise NotImplementedError("use derived class instead")
