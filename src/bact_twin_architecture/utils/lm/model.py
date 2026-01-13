"""
Todo:
    move to model submodule?
"""
from dataclasses import dataclass
from functools import cached_property
from typing import Mapping, Sequence, Union

from ...data_model.identifiers import (
    DevicePropertyID,
    ElementDevicePair,
    ElementDevicePropertyPair,
    LatticeElementPropertyID,
)


@dataclass
class LatticeElementPropertiesLUT:
    element_name: str
    lut: Mapping[str, Sequence[DevicePropertyID]]


@dataclass
class LatticeElementsPropertiesCollection:
    #: used for displaying error or debug infos
    name: str
    col: Sequence[LatticeElementPropertiesLUT]

    def get(self, name) -> Union[LatticeElementPropertiesLUT, None]:
        return self._dict.get(name, None)

    @cached_property
    def _dict(self):
        return {elem.element_name: elem for elem in self.col}


@dataclass
class DevicesPropertiesLUT:
    device_name: str
    lut: Mapping[str, Sequence[LatticeElementPropertyID]]


@dataclass
class DevicePropertiesLUTCollection:
    #: used for displaying error or debug infos
    name: str
    col: Sequence[DevicesPropertiesLUT]

    def get(self, name) -> Union[DevicesPropertiesLUT, None]:
        return self._dict.get(name, None)

    @cached_property
    def _dict(self):
        return {dev.device_name: dev for dev in self.col}


@dataclass
class ElementDevicePropertyPairsCollection:
    """one property matches to the other

    Its the same for any occurance?
    """

    name: str
    elem_dev_pairs: Sequence[ElementDevicePair]
    property_pairs: Sequence[ElementDevicePropertyPair]

    def get_element(self, name):
        return self._elem_dic.get(name, None)

    def get_device(self, name):
        return self._dev_dic.get(name, None)

    @cached_property
    def _elem_dic(self):
        return {pair.element_name: pair for pair in self.elem_dev_pairs}

    @cached_property
    def _dev_dic(self):
        return {pair.device_name: pair for pair in self.elem_dev_pairs}
