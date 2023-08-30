

from src.tictactoe.table.domain.tables import Tables
from utils.domain.singletonmeta import SingletonMeta


class CheckIsDraw(metaclass=SingletonMeta):
    
    def execute(self, table: Tables) -> bool:
        for row in table.get_table():
            for elem in row:
                if elem is Tables.EMPTY_ELEMENT:
                    return False
        return True