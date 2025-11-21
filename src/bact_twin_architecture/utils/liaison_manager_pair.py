import logging
from typing import Sequence, Union

from .model import LatticeDevicePropertyPairsCollection
from ..data_model.identifiers import LatticeElementPropertyID, DevicePropertyID
from ..interfaces.liaison_manager import LiaisonManagerBase

logger = logging.getLogger("bact-twin-architecture")


class LiaisonManagerForPairs(LiaisonManagerBase):
    def __init__(
        self,
        *,
        lut: LatticeDevicePropertyPairsCollection,
        name,
    ):
        self.name = name
        self.lut = lut

    def get_name(self) -> str:
        return self.name

    def forward(self, id_: LatticeElementPropertyID) -> Union[DevicePropertyID, None]:
        pair = self.lut.get_element(id_.element_name)
        if pair is None:
            logger.debug(
                "%s:%s(name=%s) pair lut %s: element id %s not found",
                __file__,
                self.__class__.__class__,
                self.name,
                self.lut.name,
                id_.element_name,
            )
            return None

        (dev_prop,) = [
            pp.device_property
            for pp in self.lut.property_pairs
            if id_.property == pp.element_property
        ]
        return DevicePropertyID(device_name=pair.device_name, property=dev_prop)

    def inverse(self, id_: DevicePropertyID) -> Union[LatticeElementPropertyID, None]:
        pair = self.lut.get_device(id_.device_name)
        (elem_prop,) = [
            pp.element_property
            for pp in self.lut.property_pairs
            if id_.property == pp.device_property
        ]
        return LatticeElementPropertyID(
            element_name=pair.element_name, property=elem_prop
        )
