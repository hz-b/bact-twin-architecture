from abc import abstractmethod, ABCMeta


class Identifier(metaclass=ABCMeta):
    """

    Warning:
        This identifier should not be used but one of the below

    Explicit is better than implicit
    """

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base clases")


class LatticePositionIdentifer(metaclass=ABCMeta):
    """Identifier for a certain position in e.g. a lattice"""

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base clases")


class LatticeElementIdentifer(metaclass=ABCMeta):
    """ """

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base clases")


class DeviceIdentifer(metaclass=ABCMeta):
    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base clases")
