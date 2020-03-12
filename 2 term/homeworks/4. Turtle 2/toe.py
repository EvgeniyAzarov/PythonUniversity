from figure import Figure
import turtle as t


class Toe(Figure):
    def __init__(self, x, y, d):
        super().__init__(x, y)
        self._d = d

    def _draw(self, color='blue'):
        t.up()
        t.goto(self._x + self._d / 2, self._y)
        t.color(color)
        t.down()
        t.circle(self._d / 2)
        t.up()
        t.color(t.bgcolor())

    def get_type(self):
        return 0


