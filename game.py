from exceptions import InvalidRowError, InvalidMoveError
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 1
        self.is_won = False

    def change_turn(self):
        self.turn = 2 if self.turn == 1 else 1

    def human_turn(self):
        print(f"\nPlayer {self.turn}'s turn:")
        while True:
            try:
                row_choice = int(input("Choose a row to affect (1-4): "))
                quantity = int(input("Choose how many matches to remove: "))
                self.board.move(row_choice, quantity)
                self.board.print_board()
                break
            except InvalidRowError as e:
                print(f"Invalid Row: {e}")
            except InvalidMoveError as e:
                print(f"Invalid Move: {e}")

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def best_move(self):
        possible_boards, moves = self.board.get_next_gen()
        for board, move in zip(possible_boards, moves):
            if board.get_remaining_spaces() == 1:
                return move
            if board.is_paired():
                return move
        return moves[0]

    def computer_turn(self):
        print("\nComputer's turn:")
        row, quantity = self.best_move()
        print(f"Computer removes {quantity} match(es) from row {row}.")
        self.board.move(row, quantity)
        self.board.print_board()
    
    def play_game(self):
        print("Welcome to the Uncle Game!")
        self.board.print_board()

        while not self.is_won:
            if self.turn == 1:
                self.human_turn()
            else:
                self.computer_turn()
            if self.board.get_remaining_spaces() == 0:
                self.is_won = True
                self.change_turn()
                print(f"Game over. Player {self.turn} wins!")
            else:
                self.change_turn()

game = Game()
game.play_game()
