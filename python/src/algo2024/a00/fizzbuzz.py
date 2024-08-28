def fizzbuzz(n: int):
    ''' Prints numbers from 1 to a given limit, but with a twist:
        For numbers that are multiples of 3, print "Fizz" instead of the number.
        For numbers that are multiples of 5, print "Buzz" instead of the number.
        For numbers that are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
        For all other numbers, print the number itself.'''
    for x in _fizzbuzz_arr(n):
        print(x)


def _fizzbuzz_arr(n):
    if n < 1:
        raise ValueError('n parameter should more greater than 0')
    res = []
    for x in range(1, n + 1):
        res.append(_fizzbuzz_single(x))
    
    return res


def _fizzbuzz_single(x):
    s = ''
    if x % 3 == 0:
        s = 'fizz'
    if x % 5 == 0:
        s += 'buzz'
    if s:
        return s
    else: 
        return x