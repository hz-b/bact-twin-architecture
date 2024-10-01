from abc import abstractmethod, ABCMeta


class Identifier(metaclass=ABCMeta):
    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError("implement in base clases")
