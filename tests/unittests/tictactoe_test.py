import unittest
import pytest
from unittest.mock import Mock, MagicMock

from src.tictactoe.table.application.newgame import Newgame
from src.tictactoe.table.domain.tables import Tables


class CreateGames(unittest.TestCase):

    def test_create_a_game(self):
        table = Tables(1, Tables.EMPTY_TABLE)
        mock_table_repository = Mock()
        mock_table_repository.create = MagicMock(return_value=table)
        new_game = Newgame(table_repository=mock_table_repository)
        new_table = new_game.execute()

        self.assertEqual(new_table, table)

