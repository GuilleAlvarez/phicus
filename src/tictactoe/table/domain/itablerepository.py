from abc import abstractmethod

from src.tictactoe.table.domain.tables import Tables

class ITableRepository:

    @abstractmethod
    def create(self) -> Tables:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Tables:
        pass

    @abstractmethod
    def update(self, table: Tables) -> Tables:
        pass