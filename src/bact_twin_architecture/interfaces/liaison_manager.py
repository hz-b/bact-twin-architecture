from abc import ABCMeta, abstractmethod
from typing import Sequence, Union

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
    def forward(self, id_: LatticeElementPropertyID) -> Union[Sequence[DevicePropertyID], None]:
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def inverse(self, id_: DevicePropertyID) -> Union[Sequence[LatticeElementPropertyID], None]:
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def get_name(self) -> str:
        """

        Useful for augmenting debug info as liasion managers can be
        bundled in a facade
        """
        raise NotImplementedError("use derived class instead")

