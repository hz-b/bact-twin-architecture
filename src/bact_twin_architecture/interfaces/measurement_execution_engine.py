from abc import ABCMeta, abstractmethod
from typing import Sequence

from ..data_model.command import Command


class MeasurementExecutionEngine(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, commands:  Sequence[Command]) -> str:
        """
        :return: identifier to the data
        """
        raise NotImplementedError("")
