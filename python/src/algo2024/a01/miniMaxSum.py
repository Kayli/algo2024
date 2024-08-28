#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def get_unique_indexes(n, l):
    '''generates n-sized lists of unique indexes of l-sized array'''
    indices = list(range(l))
    result = []
    def generate_unique_indexes_rec(variant: list, left: list):
        if len(variant) == n:
            result.append(variant)
            return

        for i, v in enumerate(left):
            left_clone = left[:]
            el = left_clone.pop(i)
            generate_unique_indexes_rec(variant + [el], left_clone)

    generate_unique_indexes_rec([], indices)
    return result


def miniMaxSum(arr):
    n = 4
    unique_indexes = get_unique_indexes(n, len(arr))
    vals_perms = map(lambda x: map(lambda y: arr[y], x), unique_indexes) # permutation of values of size n
    sums = list(map(lambda x: sum(x), vals_perms)) # sums of each permutation
    print(min(sums), max(sums))


    # from itertools import combinations
    # combinations_list = list(combinations(arr, 4))
    # print(combinations_list)

def miniMaxSum2(arr):
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
    miniMaxSum2([1,2,3,4,5])
