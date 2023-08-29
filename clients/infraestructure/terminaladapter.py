from clients.domain.iappclientinterface import IAppClientInterface
from src.tictactoe.table.domain.tables import Tables


class TerminalAdapter(IAppClientInterface):

    def __init__(self, handler: dict) -> None:
        self.handler = handler

    def run(self):
        table:Tables = self.handler.get("new_game")()
        print("Juego tic tac toe")
        game_over = False
        player = 0
        while(game_over is False):
            self.render_table(table)
            self.get_msg_to_play(player+1)
            (row, column) = self.get_play()
            self.handler.get("make_a_movement")(table, player, row, column)
            if (self.handler.get("check_player_win")(table, player)): break
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
    