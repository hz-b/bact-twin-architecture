"""convert the values from one state space

Todo:
    Should one have conversion a property name
"""
from abc import ABCMeta, abstractmethod
from typing import Sequence

from ..data_model.command import Command


class CommandRewriterBase(metaclass=ABCMeta):
    """alternative:
            TranslationService
    """
    @abstractmethod
    def forward(self, command: Command) -> Sequence[Command]:
        raise NotImplementedError("use derived class instead")

    @abstractmethod
    def inverse(self, command: Command) -> Sequence[Command]:
        raise NotImplementedError("use derived class instead")
