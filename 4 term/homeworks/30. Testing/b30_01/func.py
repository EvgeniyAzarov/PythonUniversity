def func(x, eps):
    assert abs(x) < 1
    assert eps > 0

    s = 0
    a = 1
    
    while abs(a) > eps:
        s += a
        a *= -x

    return s
