"""
Little example of creating iterable class in Python
Primes(n) returns a sequence of prime numbers up to n
(given number by Primes(n) cannot be more than 'n')

PS. Actually, Primes(n) returns a sequence generator!
"""

class Primes:
    def __init__(self, max_num):
        self.max_num = max_num
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._next += 1
        if self._next > self.max_num:
            self._next = 1
            raise StopIteration

        while len([x for x in range(2, 10) if self._next % x == 0 and self._next not in [2, 3, 5, 7]]) != 0:
            if self._next > self.max_num:
                self._next = 1
                raise StopIteration
            self._next += 1

        return str(self._next)


prime_nums = Primes(50)
