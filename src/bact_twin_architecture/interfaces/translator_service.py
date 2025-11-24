from abc import ABCMeta, abstractmethod
from typing import Union

from bact_twin_architecture.data_model.identifiers import ConversionID

from .state_conversion import StateConversion


class TranslatorServiceBase(metaclass=ABCMeta):
    """

    Actor says:
    * I know:

         * I want to change property "A" of lattice element "B"
         * I know that device "C" needs to change property "D"

    * please give me the translation object that converts between these
    """
    @abstractmethod
    def get(self, id_: ConversionID) -> Union[StateConversion, None]:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass