import turtle
import math

turtle.speed(0)
turtle.delay(0)

class Stem:
    def __init__(self, length=150, color="green"):
        self._length = length
        self._color = color
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(self._color)
        turtle.pensize(4)
        turtle.goto(x, y - self._length)
        turtle.pensize(1)

class Leaf:
    def __init__(self, size=30, color="forest green"):
        self._size = size
        self._color = color
    def draw(self, x, y):
        lx, ly = x, y - 60
        turtle.penup()
        turtle.goto(lx, ly)
        turtle.pendown()
        turtle.color(self._color)
        turtle.fillcolor(self._color)
        turtle.begin_fill()
        turtle.goto(lx + self._size, ly + self._size // 2)
        turtle.goto(lx + self._size * 1.5, ly + self._size)
        turtle.goto(lx + self._size // 2, ly + self._size)
        turtle.goto(lx, ly)
        turtle.end_fill()

class Petal:
    def __init__(self, size=25, color="red"):
        self._size = size
        self._color = color
    def _rotate(self, x, y, a):
        return (
            math.cos(a) * x + math.sin(a) * y,
            -math.sin(a) * x + math.cos(a) * y
        )
    def draw(self, x0, y0, angle):
        turtle.penup()
        turtle.goto(x0, y0)
        turtle.pendown()
        turtle.color(self._color)
        turtle.fillcolor(self._color)
        turtle.begin_fill()
        p1 = self._rotate(self._size, -self._size // 2, angle)
        p2 = self._rotate(self._size * 2, 0, angle)
        p3 = self._rotate(self._size, self._size // 2, angle)
        turtle.goto(x0 + p1[0], y0 + p1[1])
        turtle.goto(x0 + p2[0], y0 + p2[1])
        turtle.goto(x0 + p3[0], y0 + p3[1])
        turtle.goto(x0, y0)
        turtle.end_fill()

class Flower:
    def __init__(self, x, y, color, petals=8):
        self._x = x
        self._y = y
        self._petals = petals
        self.stem = Stem()
        self.leaf = Leaf()
        self.petal = Petal(color=color)
    def draw(self):
        self.stem.draw(self._x, self._y)
        self.leaf.draw(self._x, self._y)
        for i in range(self._petals):
            angle = i * 2 * math.pi / self._petals
            self.petal.draw(self._x, self._y, angle)

turtle.bgcolor("lightcyan")
flowers = [
    Flower(-150, 0, "crimson"),
    Flower(-80, 20, "magenta"),
    Flower(-10, 0, "orange"),
    Flower(60, 25, "purple"),
    Flower(130, 0, "deepskyblue")
]
for f in flowers:
    f.draw()
turtle.mainloop()
