import logging
from typing import Sequence, Union

from .model import ElementDevicePropertyPairsCollection
from ...data_model.identifiers import LatticeElementPropertyID, DevicePropertyID
from ...interfaces.liaison_manager import LiaisonManagerBase

logger = logging.getLogger("bact-twin-architecture")


class LiaisonManagerForPairs(LiaisonManagerBase):
    def __init__(
        self,
        *,
        lut: ElementDevicePropertyPairsCollection,
        name,
    ):
        self.name = name
        self.lut = lut

    def get_name(self) -> str:
        return self.name

    def forward(
        self, id_: LatticeElementPropertyID
    ) -> Union[Sequence[DevicePropertyID], None]:
        pair = self.lut.get_element(id_.element_name)
        if pair is None:
            logger.debug(
                "%s.%s(name=%s) pair lut %s: element id %s not found",
                __name__,
                self.__class__.__name__,
                self.name,
                self.lut.name,
                id_.element_name,
            )
            return None

        # Expecting that only a single property is found
        L = [
            pp.device_property
            for pp in self.lut.property_pairs
            if id_.property == pp.element_property
        ]
        if len(L) == 0:
            return None
        assert len(L) == 1, "Debug check: assuming that only one property is found"
        return [
            DevicePropertyID(device_name=pair.device_name, property=dev_prop)
            for dev_prop in L
        ]

    def inverse(
        self, id_: DevicePropertyID
    ) -> Union[Sequence[LatticeElementPropertyID], None]:
        pair = self.lut.get_device(id_.device_name)
        L = [
            pp.element_property
            for pp in self.lut.property_pairs
            if id_.property == pp.device_property
        ]
        if len(L) == 0:
            return None
        assert len(L) == 1, "Debug check: assuming that only one property is found"
        return [
            LatticeElementPropertyID(element_name=pair.device_name, property=dev_prop)
            for dev_prop in L
        ]
