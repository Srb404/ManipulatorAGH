class Manipulator:

    def __init__(self, a, b, c):
        self.numberA = a
        self.numberB = b
        self.numberC = c

    def nwd(self):
        biggest_factor = self.numberA
        if self.numberB > biggest_factor:
            biggest_factor = self.numberB
        if self.numberC > biggest_factor:
            biggest_factor = self.numberC

        while self.numberA % biggest_factor != 0 or self.numberB % biggest_factor != 0 or self.numberC % biggest_factor != 0:
            biggest_factor = biggest_factor - 1

        return str(biggest_factor)
