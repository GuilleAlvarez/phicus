

from src.tictactoe.table.domain.tables import Tables


class CheckPlayerWin:
    
    def execute(self, table: Tables, id_player: int) -> bool:
        return any((
            self.check_rows(table,id_player),
            self.check_columns(table,id_player),
            self.check_diagonals(table,id_player),
        ))
    
    def check_rows(self, table: Tables, id_player: int) -> bool:
        for row in table.get_table():
            if all(elem == id_player for elem in row):
                return True
        return False

    def check_columns(self, table: Tables, id_player: int) -> bool:
        number_rows = len(table.get_table())
        number_columns = len(table.get_table()[0])
        for column in range(number_columns): # iterate each column
            if all(table.get_table()[row][column] == id_player for row in range(number_rows)): # check each column
                return True
        return False

    def check_diagonals(self, table: Tables, id_player: int) -> bool:
        number_rows = len(table.get_table())
        if all(table.get_table()[index][index] == id_player for index in range(number_rows)):
            return True
        if all(table.get_table()[index][number_rows-1-index] == id_player for index in range(number_rows)):
            return True
        return False