from exceptions import InvalidMoveError
import math

class Row:
    def __init__(self, init_length):
        self.init_length = init_length
        self.matches = init_length

    def remove_match(self):
        self.matches -= 1

    def validate_move(self, quantity):
        if quantity > self.matches or quantity <= 0:
            raise InvalidMoveError("Invalid number of matches to remove.")

    def move(self, quantity):
        self.validate_move(quantity)
        for _ in range(quantity):
            self.remove_match()
                
    def get_binaries(self):      
        n = self.matches
        binary_representation = []
        if n > 0:
            power = math.floor(math.log2(n))
            while n > 0:
                current_power = 2 ** power
                if current_power <= n:
                    binary_representation.append(current_power)
                    n -= current_power
                power -= 1
        return binary_representation
