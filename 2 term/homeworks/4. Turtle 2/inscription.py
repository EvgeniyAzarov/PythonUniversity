import turtle as t

from figure import Figure


class Inscription(Figure):
    def __init__(self, x, y, text=""):
        super().__init__(x, y)
        self._text = text

    def set_text(self, text):
        self._text = text

    def _draw(self, color='black'):
        super()._draw(color)

        t.up()
        t.goto(self._x, self._y)
        t.down()
        t.color(color)
        t.write(self._text, font=("Arial", 16, "normal"), align="center")
