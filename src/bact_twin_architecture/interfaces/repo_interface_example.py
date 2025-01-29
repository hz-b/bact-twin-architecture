from abc import ABCMeta, abstractmethod
from ..data_model import user_data_model


class SomeRepo(metaclass=ABCMeta):
    @abstractmethod
    def get(self, id_: repo_id) -> user_data_model:
        """
        Todo:
            add what is not obvious from repo_id or user_data_model
        """