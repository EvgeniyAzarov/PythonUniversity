class CustomSet(set):
    def __init__(self):
        super().__init__(self)

    def add(self, el):
        if not isinstance(el, int) and \
                not isinstance(el, float) and \
                not isinstance(el, str):
            raise AttributeError

        else:
            super().add(el)


class CustomSetIterator:
    def __init__(self, collection):
        floats = []
        ints = []
        strings = []

        for c in collection:
            if isinstance(c, int):
                ints.append(c)
            elif isinstance(c, float):
                floats.append(c)
            else:
                strings.append(c)

        self._sorted = sorted(ints) + sorted(floats) + sorted(strings)
        print(self._sorted)
        self._cursor = 0

    def __next__(self):
        try:
            value = self._sorted[self._cursor]
            self._cursor += 1
            return value
        except IndexError:
            raise StopIteration
