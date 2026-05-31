import math

class Figure:
    def __init__(self):
        pass
    def dimention(self):
        raise NotImplementedError
    def perimetr(self):
        raise NotImplementedError
    def square(self):
        raise NotImplementedError
    def squareSurface(self):
        raise NotImplementedError
    def squareBase(self):
        raise NotImplementedError
    def height(self):
        raise NotImplementedError
    def volume(self):
        if self.dimention() == 2:
            return self.square()
        elif self.dimention() == 3:
            return self._volume_calc()
    def _volume_calc(self):
        raise NotImplementedError
    def __str__(self):
        return self.__class__.__name__

class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)
    def dimention(self):
        return 2
    def perimetr(self):
        return self._a + self._b + self._c
    def square(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None

class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__()
        self._a = float(a)
        self._b = float(b)
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * (self._a + self._b)
    def square(self):
        return self._a * self._b
    def squareSurface(self): return None
    def squareBase(self): return None
    def height(self): return None


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        super().__init__()
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)
        self._d = float(d)
    def dimention(self):
        return 2
    def perimetr(self):
        return self._a + self._b + self._c + self._d
    def square(self):
        diff = abs(self._a - self._b)
        if diff == 0:
            raise ValueError("Некоректна трапеція")
        x = (self._c**2 - self._d**2 + diff**2) / (2 * diff)
        h_square = self._c**2 - x**2
        if h_square < 0:
            raise ValueError("Некоректні параметри")
        h = math.sqrt(h_square)
        return ((self._a + self._b) / 2) * h
    def squareSurface(self): return None
    def squareBase(self): return None
    def height(self): return None


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        super().__init__()
        self._a = float(a)
        self._b = float(b)
        self._h = float(h)
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * (self._a + self._b)
    def square(self):
        return self._a * self._h
    def squareSurface(self): return None
    def squareBase(self): return None
    def height(self): return None

class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        self._r = float(r)
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * math.pi * self._r
    def square(self):
        return math.pi * self._r ** 2
    def squareSurface(self): return None
    def squareBase(self): return None
    def height(self): return None

class Ball(Figure):
    def __init__(self, r):
        super().__init__()
        self._r = float(r)
    def dimention(self):
        return 3
    def perimetr(self): return None
    def square(self): return Non
    def squareSurface(self):
        return 4 * math.pi * self._r ** 2
    def squareBase(self):
        return None
    def height(self):
        return None
    def _volume_calc(self):
        return (4 / 3) * math.pi * self._r ** 3

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self._h = float(h)
    def dimention(self):
        return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self):
        return super().square()
    def height(self):
        return self._h
    def squareSurface(self):
        r_in = self._a / (2 * math.sqrt(3))
        l = math.sqrt(self._h**2 + r_in**2)
        return 0.5 * super().perimetr() * l
    def _volume_calc(self):
        return (1 / 3) * self.squareBase() * self._h

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self._h = float(h)
    def dimention(self):
        return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self):
        return super().square()
    def height(self):
        return self._h
    def squareSurface(self):
        ha = math.sqrt(self._h**2 + (self._b / 2)**2)
        hb = math.sqrt(self._h**2 + (self._a / 2)**2)
        return self._a * ha + self._b * hb
    def _volume_calc(self):
        return (1 / 3) * self.squareBase() * self._h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self._c = float(c)
    def dimention(self):
        return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self):
        return super().square()
    def height(self):
        return self._c
    def squareSurface(self):
        return super().perimetr() * self._c
    def _volume_calc(self):
        return self.squareBase() * self._c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._h = float(h)
    def dimention(self):
        return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self):
        return super().square()
    def height(self):
        return self._h
    def squareSurface(self):
        l = math.sqrt(self._r**2 + self._h**2)
        return math.pi * self._r * l
    def _volume_calc(self):
        return (1 / 3) * self.squareBase() * self._h

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self._h = float(h)
    def dimention(self):
        return 3
    def perimetr(self): return None
    def square(self): return None
    def squareBase(self):
        return super().square()
    def height(self):
        return self._h
    def squareSurface(self):
        return super().perimetr() * self._h
    def _volume_calc(self):
        return self.squareBase() * self._h

def create_figure(line):
    data = line.split()
    name = data[0]
    params = list(map(float, data[1:]))
    if name == "Triangle":
        return Triangle(*params)
    elif name == "Rectangle":
        return Rectangle(*params)
    elif name == "Trapeze":
        return Trapeze(*params)
    elif name == "Parallelogram":
        return Parallelogram(*params)
    elif name == "Circle":
        return Circle(*params)
    elif name == "Ball":
        return Ball(*params)
    elif name == "TriangularPyramid":
        return TriangularPyramid(*params)
    elif name == "QuadrangularPyramid":
        return QuadrangularPyramid(*params)
    elif name == "RectangularParallelepiped":
        return RectangularParallelepiped(*params)
    elif name == "Cone":
        return Cone(*params)
    elif name == "TriangularPrism":
        return TriangularPrism(*params)
    return None

def find_max(file_name):
    figures = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                fig = create_figure(line)
                if fig:
                    figures.append(fig)
    valid_figures = []
    for f in figures:
        try:
            _ = f.volume()
            valid_figures.append(f)
        except:
            pass
    if not valid_figures:
        print("Немає коректних фігур")
        return
    best = max(valid_figures, key=lambda x: x.volume())
    print(f"\nFile: {file_name}")
    print(f"Max figure: {best}")
    print(f"Value: {best.volume():.2f}")

if __name__ == "__main__":
    find_max("input01.txt")
    find_max("input02.txt")
    find_max("input03.txt")
