

from clients.application.inputcontext import InputStartegy
from clients.infraestructure.comandclistrategy import CommandCli
from src.tictactoe.table.application.newgame import Newgame
from src.tictactoe.table.domain.itablerepository import ITableRepository
from src.tictactoe.table.domain.tables import Tables
from src.tictactoe.table.infraestructure.tablememory import TableMemory
from src.tictactoe.table.application.makemovement import MakeAMovement
from src.tictactoe.table.application.checkplayerwin import CheckPlayerWin


class App:

    def __init__(self) -> None:
        command_cli = CommandCli()
        input_strategy = InputStartegy()
        input_strategy.set_strategy(command_cli)

        self.table_repository:ITableRepository = TableMemory()
        self.new_game:Newgame = Newgame(self.table_repository)
        self.make_a_movement:MakeAMovement = MakeAMovement(self.table_repository)
        self.check_player_win:CheckPlayerWin = CheckPlayerWin()

    def run(self):
        table:Tables = self.new_game.execute()
        print("Juego tic tac toe")
        game_over = False
        player = 0
        while(game_over is False):
            self.render_table(table)
            self.get_msg_to_play(player+1)
            (row, column) = self.get_play()
            self.make_a_movement.execute(table, player, row, column)
            if (self.check_player_win.execute(table, player)): break
            player = player + 1
            player = player%2
        self.player_win(player)


    def render_table(self, table: Tables):
        for row in table.get_table():
            for elem in row:
                print(elem, end=" ")
            print()

    def get_msg_to_play(self, player):
        print(f"Es el turno del jugador: {player}")

    def get_play(self):
        row = int(input("Introduzca la fila: "))
        column = int(input("Introduzca la columna: "))
        return row, column

    def player_win(self, player):
        print(f"El jugador: {player} ha ganado")

if __name__ == "__main__":
    App().run()
