import logging
from typing import Sequence, Union, Dict

from .model import (
    TranslationObjectsForElementDevicePropertyPairsCollection,
)
from ...data_model.identifiers import ElementDevicePair, ElementDevicePropertyPair
from ...data_model.identifiers import ConversionID
from ...interfaces.state_conversion import StateConversion
from ...interfaces.translator_service import TranslatorServiceBase

logger = logging.getLogger("bact-twin-architecture")


class TranslatorServiceSharingTranslationObject(TranslatorServiceBase):
    def __init__(
        self,
        *,
        name: str,
        lut: TranslationObjectsForElementDevicePropertyPairsCollection,
        tos: Dict[str, StateConversion]
    ):
        self.name = name
        self.lut = lut
        self.tos = tos

    def get_name(self) -> str:
        return self.name

    def get(self, id_: ConversionID) -> Union[StateConversion, None]:
        pair_id = ElementDevicePair(
            element_name=id_.lattice_property_id.element_name,
            device_name=id_.device_property_id.device_name,
        )
        to_id = self.lut.get_translation_object(pair_id)
        if to_id is not None:
            r = self.tos.get(to_id.id_, None)
            if r is not None:
                return r
            logger.debug(
                "%s:%s(name=%s) pair lut %s id %s to id %s: no translation object found",
                __file__,
                self.__class__.__name__,
                self.name,
                self.lut.name,
                pair_id,
                to_id.id_,
            )
            return None

        logger.debug(
            "%s:%s(name=%s) pair lut %s id %s: no translation object found",
            __file__,
            self.__class__.__name__,
            self.name,
            self.lut.name,
            pair_id,
        )
        return None
