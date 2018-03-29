class Fibonacci(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.b = self.a + self.b
            self.a = r
            self.n = self.n + 1
            return r
        raise StopIteration


fi = Fibonacci(10)
for i in fi:
    print(i)
