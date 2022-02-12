
class ThirdQuestion:
    def __init__(self):
        pass

    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def run(self, number):
        return self.fib(number + 1)