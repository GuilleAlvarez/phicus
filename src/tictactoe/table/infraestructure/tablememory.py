from src.tictactoe.table.domain.itablerepository import ITableRepository
from src.tictactoe.table.domain.tables import Tables
from src.tictactoe.table.infraestructure.tableDTO import TablesDTO


class TableMemory(ITableRepository):

    def __init__(self) -> None:
        self.tables: [TablesDTO] = []

    def create(self) -> Tables:
        new_id = len(self.tables)
        new_table = TablesDTO.create_new_table(new_id)
        self.tables.append(new_table)
        return new_table.to_entity()
    
    def get_by_id(self, id: int) -> Tables:
        if id not in self.tables:
            return None
        return self.tables.get(id).to_entity()
    
    def update(self, table: Tables) -> Tables:
        table_dto:TablesDTO = TablesDTO.from_entity(table)
        if table_dto.get_id() not in self.tables:
            return None
        self.tables[table_dto.get_id()] = table_dto
        return table_dto.to_entity()
