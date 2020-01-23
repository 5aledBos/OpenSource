def is_odd(n):
    # comment
    # comment2
    if isinstance(n, int) is False:
        raise ValueError('Not an int')
    return n % 2 == 1


def is_even(n):
    if isinstance(n, int) is False:
        raise ValueError('Not an int')
    return n % 2 == 0


def odd_even(n):
    if is_odd(n) is True:
        return 'ODD'
    if is_even(n) is True:
        return 'EVEN'
    raise ValueError('can\'t decide')
