from abc import ABCMeta, abstractmethod
from typing import Sequence

from ..data_model.identifiers import LatticeElementPropertyID, DevicePropertyID


class LiaisonManagerBase(metaclass=ABCMeta):
    """transforms pairs of (id, property)

    Warning:
        it returns a sequence of device / properties
        More than one device can be necessary to be updated

    Todo:
        review if it violates single responsibility principle?
        Should fanout and Liaison be managed separately?
    """
    @abstractmethod
    def forward(self, id_: LatticeElementPropertyID) -> Sequence[DevicePropertyID]:
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def inverse(self, id_: DevicePropertyID) -> Sequence[LatticeElementPropertyID]:
        raise NotImplementedError("use derived class instead")
