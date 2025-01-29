from abc import ABCMeta, abstractmethod
from ..data_model.identifiers import LatticeElementPropertyID, DevicePropertyID


class LiaisonManagerBase(metaclass=ABCMeta):
    """transforms pairs of (id, property)
    """
    @abstractmethod
    def forward(self, id_: LatticeElementPropertyID) -> DevicePropertyID:
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def inverse(self, id_: DevicePropertyID) -> LatticeElementPropertyID:
        raise NotImplementedError("use derived class instead")
