from abc import abstractmethod,ABCMeta


class StateConversion(ABCMeta):
    """convert one state to an other

    Other wide spread names:
    * unit conversion
    * coordinate system transformation

    Please note initalisatin
    """
    @abstractmethod
    def forward(self, state: object) -> object:
        """from "physics" to machine

        Follows bluesky convention
        """
        raise NotImplementedError("use base claass instead")

    @abstractmethod
    def inverse(self, state: object) -> object:
        """from machine to "physics"

        Follows bluesky convention
        """
        raise NotImplementedError("use base claass instead")