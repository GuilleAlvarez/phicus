from src.tictactoe.table.domain.itablerepository import ITableRepository
from src.tictactoe.table.domain.tables import Tables
from utils.domain.singletonmeta import SingletonMeta


class Newgame(metaclass=SingletonMeta):

    def __init__(self, table_repository:ITableRepository) -> None:
        self.table_repository:ITableRepository = table_repository
    
    def execute(self) -> Tables:
        return self.table_repository.create()