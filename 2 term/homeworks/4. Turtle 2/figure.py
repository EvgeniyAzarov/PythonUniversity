import turtle as t


class Figure:
    def __init__(self, x, y):
        self._visible = False
        self._x = x
        self._y = y

    def _draw(self, color='black'):
        pass

    def show(self):
        """ Show figure on the display"""
        if not self._visible:
            self._visible = True
            self._draw()

    def hide(self):
        """ Hide figure """
        if self._visible:
            self._visible = False
            # щоб сховати фігуру, потрібно
            # зобразити її кольором фону.
            self._draw(t.bgcolor())

    def get_type(self):
        return -1
