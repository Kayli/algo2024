#!/bin/python3

from itertools import combinations


def miniMaxSum(arr):
    '''Calculates the minimum and maximum sums of n-sized combinations from the input array using itertools'''
    n = 4
    sums = [sum(comb) for comb in combinations(arr, n)]
    print(min(sums), max(sums))


def miniMaxSum_manual(arr):
    '''generates n-sized lists of unique indexes of l-sized array'''
    sums = []
    n = 4
    def generate_unique_indexes_rec(variant: list, left: list):
        if len(variant) == n:
            sums.append(sum(variant))
            return

        for i, _ in enumerate(left):
            left_clone = left[:]
            el = left_clone.pop(i)
            generate_unique_indexes_rec(variant + [el], left_clone)

    generate_unique_indexes_rec([], arr)

    print(min(sums), max(sums))


if __name__ == '__main__':
    miniMaxSum([1,2,3,4,5])
