# notes

- task description: Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

- combinatorics standard terminology
  - combination is a selection of items from a larger set where the order of the selected items does not matter
  - permutation is an arrangement of items from a set where the order of the items does matter

- python itertools functions example
  ```python
    from itertools import combinations, permutations
    items = [1, 2, 3]
    combs = list(combinations(items, 2))
    print(combs)  # Output: [(1, 2), (1, 3), (2, 3)]

    perms = list(permutations(items, 2))
    print(perms)  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
  ```
