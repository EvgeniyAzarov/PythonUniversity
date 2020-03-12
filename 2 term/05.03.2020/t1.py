from turtle import *
import random


class Figure:
    """ Клас Фігура """

    def __init__(self, x, y, color):
        """ Конструктор
        :param x: координата x положення фігури
        :param y: координата y положення фігури
        :param color: колір фігури
        """
        self._x = x  # _x - координата x
        self._y = y  # _y - координата y
        self._visible = False  # _visible - чи є фіруга видимою на екрані
        self._color = color    # _color - колір фігури

    def _draw(self, color):
        """ Допоміжний віртуальний метод, що зображує фігуру заданим кольором
        Тут здійснюється лише декларація методу, а конкретна
        реалізація буде здійснюватися у конкретних нащадках
        :param color: колір
        """
        pass

    def show(self):
        """ Зображує фігуру на екрані """
        if not self._visible:
            self._visible = True
            self._draw(self._color)

    def hide(self):
        """ Ховає фігуру (робить її невидимою на екрані) """
        if self._visible:
            self._visible = False
            # щоб сховати фігуру, потрібно
            # зобразити її кольором фону.
            self._draw(bgcolor())

    def move(self, dx, dy):
        """ Переміщує об'єкт
        :param dx: зміщення у пікселях по осі X
        :param dy: зміщення у пікселях по осі Y
        """
        isVisible = self._visible
        if isVisible:
            self.hide()
        self._x += dx
        self._y += dy
        if isVisible:
            self.show()


######################  клас Circle  ###########################
################################################################
class Circle(Figure):
    """ Клас Коло """

    def __init__(self, x, y, r, color):
        """ Конструктор
        Ініціалізує положення кола, його радіус і колір
        :param x: координата x центру кола
        :param y: координата y центру кола
        :param r: радіус кола
        :param color: колір кола
        """
        super().__init__(x, y, color)  # Обов’язковий виклик конструктора базового класу
        self._r = r  # _r - радіус кола

    def _draw(self, color):
        """ Допоміжний метод, що зображує коло заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()


#################### клас Quadrate  ############################
################################################################

class Quadrate(Figure):
    """ Клас Квадрат """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижнього кута квадрата,
        довжину його сторони і колір.
        :param x: координата x лівого нижнього кута квадрата
        :param y: координата y лівого нижнього кута квадрата
        :param a: довжина сторони квадрата
        :param color: колір квадрата
        """
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a

    def _draw(self, color):
        """ Допоміжний метод, що зображує квадрат заданим кольором
        :param color: колір
        """

        pencolor(color)
        up()

        setpos(self._x, self._y)
        down()
        for i in range(4):
            fd(self._a)
            right(90)

        up()


#################### клас Triangle  ############################
################################################################

class Triangle(Figure):
    """ Клас Трикутник
    Використовується для зображення правильного трикутника на екрані
    """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижньої вершини трикутника,
        довжину його сторони і колір.
        :param x: координата x лівої нижньої вершини трикутника
        :param y: координата y лівої нижньої вершини трикутника
        :param a: довжина сторони трикутника
        :param color: колір квадрата
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a

    def _draw(self, color):
        """ Допоміжний віртуальний метод, що зображує трикутник заданим кольором
        :param color: колір
        """

        pencolor(color)
        up()

        setpos(self._x, self._y)
        down()
        for i in range(3):
            fd(self._a)
            right(120)

        up()
#################### клас Triangle  ############################
################################################################

class Trapezoid(Figure):
    """ Клас Трапеція
    Використовується для зображення рівнобічної трапеції на екрані
    """

    def __init__(self, x, y, a, b, color):
        """ Конструктор
        Ініціалізує положення лівої нижньої вершини,
        довжини його основ і колір.
        :param x: координата x лівої нижньої вершини
        :param y: координата y лівої нижньої вершини
        :param a: довжина більшох основий трапеції
        :param b: довжина меншої основий трапеції
        :param color: колір квадрата
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a
        self._b = b

    def _draw(self, color):
        """ Віртуальний метод, що зображує трапецію на екрані заданим кольором
        :param color: колір
        """

        pencolor(color)
        up()

        setpos(self._x, self._y)
        down()
        goto(self._x + self._a / 2 - self._b / 2, self._y + self._b / 2)
        seth(0)
        fd(self._b)
        goto(self._x + self._a, self._y)
        seth(180)
        fd(self._a)

        up()


################################################################
################################################################
# Перевірка роботи описаних класів.
if __name__ == '__main__':
    # Ініціалізація turtle
    home()
    delay(30)
    speed(100)

    # ###### Перевірка кола ############
    # c = Circle(120, 120, 50, "blue")
    # c.show()
    # c.move(-30, -140)
    # c.hide()
    #
    # ###### Перевірка квадрата ############
    # q = Quadrate(0, 0, 150, "red")
    # q.show()
    # q.move(0, 140)
    # q.hide()
    #
    # ###### Перевірка трикутника ############
    # t = Triangle(120, 120, 50, "blue")
    # t.show()
    # t.move(-30, -140)
    # t.hide()

    # ###### Перевірка трапеції ############
    # t = Trapezoid(120, 120, 50, 30, "red")
    # t.show()
    # t.move(-30, -140)
    # t.hide()

    for i in range(100):
        t = random.randint(0, 3)

        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        a = random.randint(0, 100)

        rgb = (random.randint(0, 254) for j in range(3))
        color = '#{:0>2x}{:0>2x}{:0>2x}'.format(*rgb)

        if t == 0:
            c = Circle(x, y, a, color)
            c.show()
        elif t == 1:
            q = Quadrate(x, y, a, color)
            q.show()
        elif t == 2:
            t = Triangle(x, y, a, color)
            t.show()
        else:
            b = random.randint(0, 100)
            t = Trapezoid(x, y, a, b, color)
            t.show()

    mainloop()