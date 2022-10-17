from abc import ABC, abstractmethod


class IReadFile(ABC):

    @abstractmethod
    def readjson(self, file_path):
        pass

    @abstractmethod
    def readxml(self, file_path):
        pass
