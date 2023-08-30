from clients.domain.iappclientinterface import IAppClientInterface
from src.tictactoe.table.domain.tables import Tables
from utils.domain.singletonmeta import SingletonMeta


class TerminalAdapter(IAppClientInterface, metaclass=SingletonMeta):

    def __init__(self, handler: dict) -> None:
        self.handler = handler

    def run(self):
        print("Juego tic tac toe")
        is_playing = input("Pulse 0 para salir, o pulse otra tecla para jugar: ")
        while is_playing!="0":
            self.play_a_match()

    def play_a_match(self):
        table:Tables = self.handler.get("new_game")()
        game_over = False
        player = 0
        while(game_over is False):
            self.render_table(table)
            self.get_msg_to_play(player+1)
            try:
                self.make_a_move(table, player)
            except ValueError as e:
                print(e)
                continue
            if (self.handler.get("check_player_win")(table, player)):
                self.player_win(player)
                break
            if (self.handler.get("check_is_draw")(table)):
                self.draw()
                break
            player = (player+1)%2


    def render_table(self, table: Tables):
        for row in table.get_table():
            for elem in row:
                print(elem, end=" ")
            print()

    def get_msg_to_play(self, player):
        print(f"Es el turno del jugador: {player}")

    def make_a_move(self, table, player):
        (row, column) = self.get_move()
        self.handler.get("make_a_movement")(table, player, row, column)

    def get_move(self):
        try:
            row = int(input("Introduzca la fila: "))
            column = int(input("Introduzca la columna: "))
        except ValueError as e:
            raise ValueError("Debe introducir números del 0 al 2!!")
        return row, column
    
    def player_win(self, player):
        print(f"¡¡El jugador: {player} ha ganado!!")

    def draw(self):
        print(f"¡¡El juego ha terminado: ha sido un empate!!")
    