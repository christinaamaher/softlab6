
class SquareCalculator:
    def area(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        return side_length * side_length

