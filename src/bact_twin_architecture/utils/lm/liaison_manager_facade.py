"""Liaison manager implementation often used

Todo:
    These implementations show once more that forward and backward
    should just be gets
"""
import logging
from typing import Sequence, Mapping, Union

from ...data_model.identifiers import LatticeElementPropertyID, DevicePropertyID
from ...interfaces.liaison_manager import LiaisonManagerBase

logger = logging.getLogger("bact-twin-architecture")


class LiaisonManagerFacade(LiaisonManagerBase):
    """

    Tries resolving an answer depending on the different liaison managers
    available

    Note:
        you can stack LiaisonManagerFacades as you like
    """

    def __init__(self, *, delegates: Sequence[LiaisonManagerBase], name: str):
        self.delegates = delegates
        self.name = name

    def get_name(self):
        return self.name

    def forward(
        self, id_: LatticeElementPropertyID
    ) -> Union[Sequence[DevicePropertyID], None]:
        """

        Todo:
            delegates will raise an Exception if no answer is found
            Shall that stay in this manner ?

            Furthermore: only return one answer?
            The first one returned?

            Assuming that user will provide the most specific first and then
            the more general ones further one

            How to report that no answer was found? Shall one only then start to
            ask the different delegates which would be the closest possible match?
            The advantage would be that one does not loose time during look up as
            no answer for a single delegate could be appropriate.

        """
        for delegate in self.delegates:
            r = delegate.forward(id_)
            if r is not None:
                logger.info(
                    "%s.%s(name=%s) fwd mapping %s -> %s",
                    __name__,
                    self.__class__.__name__,
                    self.name,
                    id_,
                    r,
                )
                return r
        else:
            logger.warning(
                "%s.%s(name=%s) no mapping found for %s in one of the liaison managers %s",
                __name__,
                self.__class__.__name__,
                self.name,
                id_,
                [lm.get_name() for lm in self.delegates],
            )
            return None

    def inverse(
        self, id_: DevicePropertyID
    ) -> Union[Sequence[LatticeElementPropertyID], None]:
        for delegate in self.delegates:
            r = delegate.inverse(id_)
            if r is not None:
                logger.info(
                    "%s.%s(name=%s) fwd mapping %s -> %s",
                    __name__,
                    self.__class__.__name__,
                    self.name,
                    id_,
                    r,
                )
                return r
        else:
            logger.warning(
                f"%s.%s(name=%s) no mapping found for %s in any liaison manager %s",
                __name__,
                self.__class__.__name__,
                self.name,
                id_,
                [lm.get_name() for lm in self.delegates],
            )
            return None
