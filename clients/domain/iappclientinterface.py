
from abc import abstractmethod


class IAppClientInterface:

    @abstractmethod
    def run(self):
        pass
