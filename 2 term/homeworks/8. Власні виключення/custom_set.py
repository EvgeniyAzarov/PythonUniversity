class CustomSet():
    def __init__(self):
        self._ints = set()
        self._floats = set()
        self._strings = set()

    def add(self, el):
        if not isinstance(el, int) and \
                not isinstance(el, float) and \
                not isinstance(el, str):
            raise CustomSetError(type(el).__name__)
        if isinstance(el, int):
            self._ints.add(el)
        elif isinstance(el, float):
            self._floats.add(el)
        elif isinstance(el, str):
            self._strings.add(el)

    def __iter__(self):
        return CustomSetIterator(self)


class CustomSetIterator:
    def __init__(self, collection):
        self._sorted = sorted(list(collection._ints)) + \
                       sorted(list(collection._floats)) + \
                       sorted(list(collection._strings))
        self._cursor = 0

    def __next__(self):
        try:
            value = self._sorted[self._cursor]
            self._cursor += 1
            return value
        except IndexError:
            raise StopIteration


class CustomSetError(TypeError):
    def __init__(self, invalid_type):
        super().__init__()
        self.invalid_type = invalid_type

    def __str__(self):
        return "Invalid object type \n" + \
               "\texpected: int, float or string \n" + \
               "\tfound: " + str(self.invalid_type)

