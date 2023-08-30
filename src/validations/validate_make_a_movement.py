

class ValidateMakeAMovement:

    @staticmethod
    def basic_validate(row: int, column: int):
        if not (0 <= row <= 2):
            raise ValueError("Debe introducir números del 0 al 2!!")
        if not (0 <= column <= 2):
            raise ValueError("Debe introducir números del 0 al 2!!")
        return True