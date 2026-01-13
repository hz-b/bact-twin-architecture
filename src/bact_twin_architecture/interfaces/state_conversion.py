"""

Todo:
    review if the type of the state objects can be further
    limited:

    e.g. Dict[str, float|int|bool|str]

    for single value str should be then default
"""
from abc import abstractmethod, ABCMeta


class StateConversion(metaclass=ABCMeta):
    """convert one state to an other

    Other wide spread names:
    * unit conversion
    * coordinate system transformation

    Please note initialisation is not handled here

    Todo:
       Shall one add the command conversion here too?
       It seems to violate the single objective principle.
    """

    @abstractmethod
    def forward(self, state: object) -> object:
        """from "physics" to machine

        Follows bluesky convention
        """
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def inverse(self, state: object) -> object:
        """from machine to "physics"

        Follows bluesky convention
        """
        raise NotImplementedError("use derived class instead")
