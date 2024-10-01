from abc import abstractmethod, ABCMeta


class LatticePositionIdentifier(metaclass=ABCMeta):
    """Identifier for a certain position in e.g. a lattice"""

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base class")


class LatticeElementIdentifier(metaclass=ABCMeta):
    """ """

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base class")


class DeviceIdentifier(metaclass=ABCMeta):
    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base class")
