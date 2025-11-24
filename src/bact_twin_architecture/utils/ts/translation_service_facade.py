import logging
from typing import Sequence, Union

from ...data_model.identifiers import ConversionID
from ...interfaces.state_conversion import StateConversion
from ...interfaces.translator_service import TranslatorServiceBase

logger = logging.getLogger("bact-twin-architecture")


class TranslatorServiceFacade(TranslatorServiceBase):
    def __init__(self, *, name: str, delegates: Sequence[TranslatorServiceBase]):
        self.name = name
        self.delegates = delegates

    def get_name(self) -> str:
        return self.name

    def get(self, id_: ConversionID) -> Union[StateConversion, None]:

        for delegate in self.delegates:
            r = delegate.get(id_)
            if r is not None:
                logger.info(
                    f"%s:%s(name=%s).get(%s): to %s",
                    __file__,
                    self.__class__.__name__,
                    self.name,
                    id_,
                    r,
                )
                return r
        else:
            logger.warning(
                f"%s:%s(name=%s).get(%s) using delegates %s found no translation object ",
                __file__,
                self.__class__.__name__,
                self.name,
                [lm.get_name() for lm in self.delegates],
                id_,
            )
            return None
