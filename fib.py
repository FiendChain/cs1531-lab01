'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

# cache fibonacci
fibonacci_cache = {}
def get_fib(n):
    if n <= 2:
        if n not in fibonacci_cache:
            fibonacci_cache[n] = 1
    elif n not in fibonacci_cache:
        fibonacci_cache[n] = get_fib(n-1) + get_fib(n-2)
    return fibonacci_cache[n]
    

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    return [get_fib(i) for i in range(1,n+1)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
