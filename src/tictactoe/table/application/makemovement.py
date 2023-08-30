from src.tictactoe.table.domain.itablerepository import ITableRepository
from src.tictactoe.table.domain.tables import Tables
from src.validations.validate_make_a_movement import ValidateMakeAMovement


class MakeAMovement:

    def __init__(self, table_repository:ITableRepository) -> None:
        self.table_repository:ITableRepository = table_repository
    
    def execute(self, table: Tables, id_player: int, row: int, column: int) -> Tables:
        self.validate(table, row, column)
        table.update_table(id_player=id_player, row=row, column=column)
        return self.table_repository.update(table)
    
    def validate(self, table: Tables, row: int, column: int):
        ValidateMakeAMovement.basic_validate(row, column)
        if not table.is_empty(row, column):
             raise ValueError("Esa casilla ya esta ocupada!!")

