import turtle as t

from figure import Figure


class Board(Figure):
    def __init__(self, s, w):
        super().__init__(0, 0)
        self._s = s
        self._w = w

    def _draw(self, x=0, y=0):
        t.up()
        t.goto(x - self._s / 2, y - self._s / 2)
        t.seth(90)
        t.width(self._w)

        t.down()

        for i in range(4):
            t.fd(self._s)
            t.right(90)

        for i in range(2):
            t.up()
            t.goto(x - self._s / 2, y - self._s / 2 + (i + 1) * self._s / 3)
            t.seth(0)
            t.down()
            t.fd(self._s)

        for i in range(2):
            t.up()
            t.goto(x - self._s / 2 + (i + 1) * self._s / 3, y - self._s / 2)
            t.seth(90)
            t.down()
            t.fd(self._s)

        t.width(3)
