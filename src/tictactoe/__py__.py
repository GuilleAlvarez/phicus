from abc import abstractmethod


class DatabaseFactory:

    @abstractmethod
    def get_database():
        return ""