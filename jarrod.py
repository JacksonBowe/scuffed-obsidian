

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    print('why')
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    print('yo')
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    print('here')
    # yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                # yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

x = permutations(['a', 'b', 'c'])
print(x)