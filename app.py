from clients.infraestructure.httpadapter import HttpAdapter
from clients.infraestructure.terminaladapter import TerminalAdapter
from src.tictactoe.table.application.newgame import Newgame
from src.tictactoe.table.domain.itablerepository import ITableRepository
from src.tictactoe.table.domain.tables import Tables
from src.tictactoe.table.infraestructure.tablememory import TableMemory
from src.tictactoe.table.application.makemovement import MakeAMovement
from src.tictactoe.table.application.checkplayerwin import CheckPlayerWin
from src.tictactoe.table.application.checkisdraw import CheckIsDraw


class App:

    def __init__(self) -> None:

        self.table_repository:ITableRepository = TableMemory()
        self.new_game:Newgame = Newgame(self.table_repository)
        self.make_a_movement:MakeAMovement = MakeAMovement(self.table_repository)
        self.check_player_win:CheckPlayerWin = CheckPlayerWin()
        self.check_is_draw:CheckIsDraw = CheckIsDraw()

    def run(self):
        handler = {
            "new_game": self.new_game.execute,
            "make_a_movement": self.make_a_movement.execute,
            "check_player_win": self.check_player_win.execute,
            "check_is_draw": self.check_is_draw.execute
        }
        TerminalAdapter(handler).run()

if __name__ == "__main__":
    App().run()
