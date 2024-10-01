from abc import abstractmethod, ABCMeta


class LatticePositionIdentifierObsolete(metaclass=ABCMeta):
    """Identifier for a certain position in e.g. a lattice"""

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base class")


class LatticeElementIdentifierObsolete(metaclass=ABCMeta):
    """ """

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base class")


class DeviceIdentifierObsolete(metaclass=ABCMeta):
    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base class")
