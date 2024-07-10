class Prime:
    def __init__(self):
        self.factors = []
        self.divisor = 2

    def of(self, number) -> list:
        while number > 1:
            while number % self.divisor == 0:
                self.factors.append(self.divisor)
                number /= self.divisor
            self.divisor += 1
        return self.factors

