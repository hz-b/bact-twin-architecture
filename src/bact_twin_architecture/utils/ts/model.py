from dataclasses import dataclass
from functools import cached_property
from typing import Sequence, Union

from ...data_model.identifiers import ElementDevicePair, ElementDevicePropertyPair


@dataclass
class TranslationObjectsForElementDevicePropertyPairs:
    id_: str
    property_pair: ElementDevicePropertyPair


@dataclass
class TranslationObjectsForElementDevicePropertyPairsCollection:
    """For objects that share the same translation object for the
    same properties
    """

    name: str
    elem_dev_pairs: Sequence[ElementDevicePair]
    translation_object_ids: Sequence[TranslationObjectsForElementDevicePropertyPairs]

    def get_translation_object(
        self, dev_elem_pair: ElementDevicePair, prop_pair: ElementDevicePropertyPair
    ) -> Union[TranslationObjectsForElementDevicePropertyPairs, None]:
        # Todo: worth while to use dict look up?
        if dev_elem_pair in self.elem_dev_pairs:
            return self._to_dic.get(prop_pair, None)

    @cached_property
    def _to_dic(self):
        return {to_id.property_pair: to_id for to_id in self.translation_object_ids}
