from src.tictactoe.table.domain.itablerepository import ITableRepository
from src.tictactoe.table.domain.tables import Tables


class Newgame:

    def __init__(self, table_repository:ITableRepository) -> None:
        self.table_repository:ITableRepository = table_repository
    
    def execute(self) -> Tables:
        return self.table_repository.create()