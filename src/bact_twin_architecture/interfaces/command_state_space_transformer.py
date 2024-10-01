"""convert the values from one state space

Todo:
    Should one have conversion a property name
"""
from abc import ABCMeta, abstractmethod

from ..data_model.command import Command


class StateSpaceTransformer(metaclass=ABCMeta):
    @abstractmethod
    def forward(self, command: Command):
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def backward(self, command: Command):
        raise NotImplementedError("use derived class instead")
