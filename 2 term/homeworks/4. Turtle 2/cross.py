from figure import Figure
import turtle as t


class Cross(Figure):
    def __init__(self, x, y, d):
        super().__init__(x, y)
        self._l = d

    def _draw(self, color='red'):
        t.color(color)
        t.up()
        t.goto(self._x - self._l / 2, self._y + self._l / 2)
        t.down()
        t.goto(self._x + self._l / 2, self._y - self._l / 2)
        t.up()
        t.goto(self._x + self._l / 2, self._y + self._l / 2)
        t.down()
        t.goto(self._x - self._l / 2, self._y - self._l / 2)
        t.up()
        t.color(t.bgcolor())

    def get_type(self):
        return 1


