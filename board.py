from exceptions import InvalidRowError, InvalidMoveError
from row import Row
import copy

class Board:
    def __init__(self):
        self.rows = self.get_rows()

    def get_rows(self):
        rows = []
        rows_amount = int(input("How many rows do you want to play with? "))
        for row_index in range(rows_amount):
            rows.append(Row(int(input(f"How many matches do you want in row {row_index + 1}: "))))
        return rows
                        
    def get_remaining_spaces(self):
        return sum(row.matches for row in self.rows)
    
    def validate_row(self, row):
        if row < 1 or row > len(self.rows):
            raise InvalidRowError("Invalid row number. Choose between 1 and 4.")

    def move(self, row, quantity):
        self.validate_row(row)
        self.rows[row - 1].move(quantity)

    def print_board(self):
        print("\nCurrent Board:")
        for i, row in enumerate(self.rows):
            print(f"{i+1}: {' |' * row.matches}")

    def get_binaries(self):
        binary_board = []
        for row in self.rows:
            binary_board.extend(row.get_binaries())
        return binary_board

    def remove_pairs(self):
        temp_board = copy.deepcopy(self.get_binaries())
        temp_board.sort()
        i = 0
        while i < len(temp_board) - 1:
            if temp_board[i] == temp_board[i + 1]:
                temp_board.pop(i)
                temp_board.pop(i)
            else:
                i += 1
        return temp_board

    def is_paired(self):
        return self.remove_pairs() == []

    def get_next_gen(self):
        possible_boards = []
        moves = []
        for i, row in enumerate(self.rows, start=1):
            for amount in range(1, row.matches + 1):
                board = copy.deepcopy(self)
                try:
                    board.move(i, amount)
                    possible_boards.append(board)
                    moves.append((i, amount))
                except InvalidMoveError:
                    continue
        return possible_boards, moves
