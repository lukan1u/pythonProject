from typing import NamedTuple
import numpy
import timeit

def sum_range(n = 100_000_000):
    return sum(range(n))

def for_loop(n = 100_000_000):
    return numpy.sum(numpy.arange(n))

def main():
    print("sum range\t", timeit.timeit(sum_range, number = 1))
    print("sum numpy\t", timeit.timeit(for_loop, number = 1))


if __name__ == '__main__':
    main()
