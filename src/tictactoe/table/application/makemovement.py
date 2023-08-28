from src.tictactoe.table.domain.itablerepository import ITableRepository
from src.tictactoe.table.domain.tables import Tables


class MakeAMovement:

    def __init__(self, table_repository:ITableRepository) -> None:
        self.table_repository:ITableRepository = table_repository
    
    def execute(self, table: Tables, id_player: int, row: int, column: int) -> Tables:
        table.update_table(id_player=id_player, row=row, column=column)
        return self.table_repository.update(table)