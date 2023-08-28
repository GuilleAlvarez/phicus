

class Tables:

    EMPTY_ELEMENT = None
    EMPTY_TABLE:list = [
        [EMPTY_ELEMENT,EMPTY_ELEMENT,EMPTY_ELEMENT],
        [EMPTY_ELEMENT,EMPTY_ELEMENT,EMPTY_ELEMENT],
        [EMPTY_ELEMENT,EMPTY_ELEMENT,EMPTY_ELEMENT]
    ]

    def __init__(self, id: int, table: list) -> None:
        self.id = id
        self.table = table

    def get_id(self) -> int:
        return self.id

    def get_table(self) -> list:
        return self.table
    
    def update_table(self, id_player:int, row: int, column: int):
        self.table[row][column] = id_player


    @staticmethod
    def create_new_table():
        return Tables