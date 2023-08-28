from src.tictactoe.table.domain.tables import Tables


class TablesDTO:

    def __init__(self, id: int, table: list) -> None:
        self.id = id
        self.table = table

    @staticmethod
    def create_new_table(id, 
        table=Tables.EMPTY_TABLE):
        return TablesDTO(id, table)
    
    @staticmethod
    def from_entity(table:Tables):
        return TablesDTO(table.get_id(), table.get_table())
    
    def get_id(self) -> int:
        return self.id

    def to_entity(self) -> Tables:
        return Tables(self.id, self.table)
