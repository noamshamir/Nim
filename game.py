from exceptions import InvalidRowError, InvalidMoveError
from board import Board
import random

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 1
        self.is_won = False
        self.eval = 0

    def change_turn(self):
        self.turn = 2 if self.turn == 1 else 1

    def human_turn(self):
        print(f"\nPlayer {self.turn}'s turn:")
        while True:
            try:
                row_choice = int(input(f"Choose a row to affect (1-{len(self.board.rows)}): "))
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
                self.eval = 1
                return move
        for board, move in zip(possible_boards, moves):
            if board.is_paired():
                self.eval = 1
                return move
        self.eval = -1
        return moves[random.randint(0, len(moves))]

    def computer_turn(self):
        print("\nComputer's turn:")
        row, quantity = self.best_move()
        print(f"Computer removes {quantity} match(es) from row {row}.")
        print(f"Computer predicts a score of {self.eval}")
        self.board.move(row, quantity)
        self.board.print_board()
    
    def play_game(self):
        print("")
        print("Let's play Nim!")
        self.board.print_board()

        while not self.is_won:
            if self.turn == 1:
                self.computer_turn()
            else:
                self.human_turn()
            if self.board.get_remaining_spaces() == 0:
                self.is_won = True
                self.change_turn()
                print(f"Game over. Player {self.turn} wins!")
            else:
                self.change_turn()

game = Game()
game.play_game()