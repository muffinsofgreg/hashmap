from random import choice
import matplotlib.pyplot as plt


class PlotMap:
    """Generates a visual chart, plotting the hash indexes on the control axis
       and the number of hashed items on the dependent axis
    """

    def __init__(self, map):
        self.map = map

    def visualize(self, map):

        plt.figure('Visual Map')

        plt.clf()

        n, bins, patches = plt.hist(len(map), [item for item in map])

        plt.show()


class Prime_Generator:
    """Generates a series of prime numbers up to N"""

    def __init__(self, n):
        self._n = n
        self._a = self._create_sieve(n)
        self._list = self._generate_list()

    def _create_sieve(self, size):

        a = []
        for i in range(2, size + 1):
            a.append(i)

        return a

    def _sieve_of_eratosthenes(self, list):
        size = len(list)
        for i in list:
            j = 2
            while j <= size:
                for k in range(1, size + 1):
                    j = i**2
                    try:
                        list.remove(j)
                    except ValueError:
                        pass
                    j = (i**2) + (k * i)
                    try:
                        list.remove(j)
                    except ValueError:
                        pass

        return list

    def _generate_list(self):
        return self._sieve_of_eratosthenes(self._a)

    @property
    def prime_list(self):
        return self._list

    def rand_prime(self):
        return choice(self.prime_list)


if __name__ == "__main__":

    print("Sieve of Eratosthenes Prime Number Generator\n")
    N = int(input('Will generate all of the primes up to N.\nWhat is your N: '))
    gen = Prime_Generator(N)
    print(f'Your Prime List: \n{gen.prime_list}')
