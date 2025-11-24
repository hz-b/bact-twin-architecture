import logging
from typing import Sequence, Union

from .model import LatticeElementsPropertiesCollection, DevicePropertiesLUTCollection
from ...data_model.identifiers import LatticeElementPropertyID, DevicePropertyID
from ...interfaces.liaison_manager import LiaisonManagerBase

logger = logging.getLogger("bact-twin-architecture")


class LiaisonManagerForFamily(LiaisonManagerBase):
    def __init__(
        self,
        forward_lut: LatticeElementsPropertiesCollection,
        inverse_lut: DevicePropertiesLUTCollection,
        name,
    ):
        self.forward_lut = forward_lut
        self.inverse_lut = inverse_lut
        self.name = name

    def get_name(self):
        return self.name

    def forward(
        self, id_: LatticeElementPropertyID
    ) -> Union[Sequence[DevicePropertyID], None]:
        elem_lut = self.forward_lut.get(id_.element_name)
        if elem_lut is None:
            logger.debug(
                "%s.%s(name=%s) family lut %s: element %s not found",
                __name__,
                self.__class__.__name__,
                self.name,
                self.forward_lut.name,
                id_.element_name,
            )
            return None

        r = elem_lut.lut.get(id_.property, None)
        if r is None:
            logger.debug(
                "%s.%s(name=%s) family lut %s element %s: %s not found",
                __name__,
                self.__class__.__name__,
                self.name,
                self.forward_lut.name,
                id_.element_name,
                id_.property,
            )

        return r

    def inverse(
        self, id_: DevicePropertyID
    ) -> Union[Sequence[LatticeElementPropertyID], None]:
        elem_lut = self.inverse_lut.get(id_.device_name)
        if elem_lut is None:
            logger.debug(
                "%s.%s(name=%s) family lut %s: device %s not found",
                __name__,
                self.__class__.__name__,
                self.name,
                self.inverse_lut.name,
                id_.device_name,
            )
            return None

        r = elem_lut.lut.get(id_.property, None)
        if r is None:
            logger.debug(
                "%s.%s(name=%s) family lut %s device %s: property %s not found",
                __name__,
                self.__class__.__name__,
                self.name,
                self.inverse_lut.name,
                id_.device_name,
                id_.property,
            )
            return None
        return r
