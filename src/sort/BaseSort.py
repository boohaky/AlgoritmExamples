from abc import ABC, abstractmethod


class BaseSort(ABC):

    @abstractmethod
    def sort(self, list_to_sort):
        pass
