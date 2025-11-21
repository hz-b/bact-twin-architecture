import logging
from typing import Mapping, Sequence, Union

from ..data_model.identifiers import LatticeElementPropertyID, DevicePropertyID
from ..interfaces.liaison_manager import LiaisonManagerBase

logger = logging.getLogger("bact-twin-architecture")


class LiaisonManagerOnlyLookup(LiaisonManagerBase):
    """The classic liaison manager look request uo in a repository or dictonary"""

    def __init__(
        self,
        *,
        forward_lut: Mapping[
            LatticeElementPropertyID, Sequence[DevicePropertyID]
        ] = None,
        inverse_lut: Mapping[
            DevicePropertyID, Sequence[LatticeElementPropertyID]
        ] = None,
        name: str,
    ):
        self.forward_lut = forward_lut
        self.inverse_lut = inverse_lut
        self.name = name

    def get_name(self):
        return self.name

    def forward(
        self, id_: LatticeElementPropertyID
    ) -> Union[Sequence[DevicePropertyID], None]:
        r = self.forward_lut.get(id_, None)
        if r is None:
            logger.debug(
                "%s:%s(name=%s) id %s not found in lookup table:",
                __file__,
                self.__class__.__class__,
                self.name,
                id_,
            )
        else:
            logger.debug(
                f"%s:%s(name=%s) fwd mapping %s -> %s",
                __file__,
                self.__class__.__class__,
                self.name,
                id_,
                r,
            )
        return r

    def inverse(
        self, id_: DevicePropertyID
    ) -> Union[Sequence[LatticeElementPropertyID], None]:
        r = self.inverse_lut.get(id_, None)
        if r is None:
            logger.info(
                "%s:%s(name=%s) id %s not found in lookup table:",
                __file__,
                self.__class__.__class__,
                self.name,
                id_,
            )
        else:
            logger.debug(
                f"%s:%s(name=%s) fwd mapping %s -> %s",
                __file__,
                self.__class__.__class__,
                self.name,
                id_,
                r,
            )
        return r
