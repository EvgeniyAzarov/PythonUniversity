def input_type(perm_type) :
    def _input_type_(f):
        def __input_type__(*args, **kwargs):
            all_args = args + tuple(kwargs.values())
            for arg in all_args:
                if not type(arg) is perm_type:
                    raise KeyError(
                        "Argument \'{}\' must be of type {}" \
                            .format(arg, perm_type)
                    )
                    break
            else:
                res = f(*args, **kwargs)
                return res

        return __input_type__
    return _input_type_


@input_type(float)
def amean(*args, **kwargs):
    a = args + tuple(kwargs.values())
    s = 0
    for x in a:
        s += x
    return s / len(a)


if __name__ == '__main__':
    print(amean(1.1, 1.2))
    print(amean('a', 1, 2, 3))
    print(amean(1, 2, 3))
