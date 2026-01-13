import logging
from typing import Union, Mapping

from ...data_model.identifiers import ConversionID
from ...interfaces.state_conversion import StateConversion
from ...interfaces.translator_service import TranslatorServiceBase

logger = logging.getLogger("bact-twin-architecture")


class TranslatorServiceLUT(TranslatorServiceBase):
    def __init__(
        self,
        *,
        name: str,
        lut: Mapping[ConversionID, StateConversion],
    ):
        self.name = name
        self.lut = lut

    def get_name(self) -> str:
        return self.name

    def get(self, id_: ConversionID) -> Union[StateConversion, None]:
        r = self.lut.get(id_, None)
        if r is not None:
            return r

        logger.debug(
            "%s:%s(name=%s) pair lut %s id %s: no translation object found",
            __file__,
            self.__class__.__name__,
            self.name,
            id_,
        )

    def objects_for_lat_elem(self, element_name: str):
        """
        Todo:
            is this method helpful for debug purposes ?
        """
        return {
            key: to
            for key, to in self.lut.items()
            if element_name == key.lattice_property_id.element_name
        }

    def objects_for_device(self, device_name: str):
        """
        Todo:
            is this method helpful for debug purposes ?
        """
        return {
            key: to
            for key, to in self.lut.items()
            if device_name == key.device_property_id.device_name
        }
