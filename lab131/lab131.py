import math

class FigureInfo:
    def __init__(self, area_value, perimeter_value, is_valid):
        self._area = area_value
        self._perimeter = perimeter_value
        self._is_valid = is_valid
    def is_valid(self):
        return self._is_valid
    def get_area(self):
        return self._area
    def get_perimeter(self):
        return self._perimeter

class Figure:
    def __init__(self, name):
        self._name = name
    def area(self):
        return 0
    def perimeter(self):
        return 0
    def get_name(self):
        return self._name
    def get_info(self):
        area_value = self.area()
        perimeter_value = self.perimeter()
        if area_value < 0 or perimeter_value < 0:
            return FigureInfo(0, 0, False)
        return FigureInfo(
            area_value,
            perimeter_value,
            True
        )

class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self._a = a
        self._b = b
        self._c = c
    def is_valid_triangle(self):
        return (
            self._a > 0 and
            self._b > 0 and
            self._c > 0 and
            self._a + self._b > self._c and
            self._a + self._c > self._b and
            self._b + self._c > self._a
        )
    def perimeter(self):
        if not self.is_valid_triangle():
            return -1
        return self._a + self._b + self._c
    def area(self):
        if not self.is_valid_triangle():
            return -1
        p = self.perimeter() / 2
        return math.sqrt(
            p *
            (p - self._a) *
            (p - self._b) *
            (p - self._c)
        )
    def __str__(self):
        return (
            f"Triangle("
            f"{self._a}, "
            f"{self._b}, "
            f"{self._c})"
        )

class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__("Rectangle")
        self._a = a
        self._b = b
    def perimeter(self):
        if self._a <= 0 or self._b <= 0:
            return -1
        return 2 * (self._a + self._b)
    def area(self):
        if self._a <= 0 or self._b <= 0:
            return -1
        return self._a * self._b
    def __str__(self):
        return (
            f"Rectangle("
            f"{self._a}, "
            f"{self._b})"
        )
      
class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        super().__init__("Trapeze")
        self._a = a
        self._b = b
        self._c = c
        self._d = d
    def is_valid_trapeze(self):
        if (
            self._a <= 0 or
            self._b <= 0 or
            self._c <= 0 or
            self._d <= 0
        ):
            return False

        diff = abs(self._a - self._b)

        if diff == 0:
            return False
        return (
            abs(self._c - self._d)
            < diff <
            self._c + self._d
        )

    def perimeter(self):
        if not self.is_valid_trapeze():
            return -1
        return (
            self._a +
            self._b +
            self._c +
            self._d
        )
    def area(self):
        if not self.is_valid_trapeze():
            return -1
        diff = abs(self._a - self._b)
        x = (
            self._c**2 -
            self._d**2 +
            diff**2
        ) / (2 * diff)
        h_squared = self._c**2 - x**2
        if h_squared < 0:
            return -1
        h = math.sqrt(h_squared)
        return (
            (self._a + self._b)
            * h / 2
        )
    def __str__(self):
        return (
            f"Trapeze("
            f"{self._a}, "
            f"{self._b}, "
            f"{self._c}, "
            f"{self._d})"
        )

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        super().__init__("Parallelogram")
        self._a = a
        self._b = b
        self._h = h
    def is_valid_parallelogram(self):
        return (
            self._a > 0 and
            self._b > 0 and
            self._h > 0 and
            self._h <= self._b
        )
    def perimeter(self):
        if not self.is_valid_parallelogram():
            return -1
        return 2 * (
            self._a +
            self._b
        )
    def area(self):
        if not self.is_valid_parallelogram():
            return -1
        return self._a * self._h
    def __str__(self):
        return (
            f"Parallelogram("
            f"{self._a}, "
            f"{self._b}, "
            f"{self._h})"
        )

class Circle(Figure):
    def __init__(self, r):
        super().__init__("Circle")
        self._r = r
    def perimeter(self):
        if self._r <= 0:
            return -1
        return 2 * math.pi * self._r
    def area(self):
        if self._r <= 0:
            return -1
        return math.pi * self._r**2
    def __str__(self):
        return f"Circle({self._r})"


def analyze_file(file_name):
    my_objects = []
    figure_classes = {
        "Triangle": Triangle,
        "Rectangle": Rectangle,
        "Trapeze": Trapeze,
        "Parallelogram": Parallelogram,
        "Circle": Circle
    }
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) == 0:
                    continue
                figure_name = parts[0]
                values = []
                for x in parts[1:]:
                    values.append(float(x))
                if figure_name in figure_classes:
                    try:
                        obj = figure_classes[
                            figure_name
                        ](*values)
                        my_objects.append(obj)
                    except TypeError:
                        pass
    except FileNotFoundError:
        print(
            "File not found:",
            file_name
        )
        return
    max_area = -1
    max_perimeter = -1
    best_area_shape = None
    best_perimeter_shape = None
    for obj in my_objects:
        info = obj.get_info()
        if info.is_valid():
            if (
                info.get_area()
                > max_area
            ):
                max_area = (
                    info.get_area()
                )
                best_area_shape = obj
            if (
                info.get_perimeter()
                > max_perimeter
            ):
                max_perimeter = (
                    info.get_perimeter()
                )
                best_perimeter_shape = obj
    print("\nFile:", file_name)
    if best_area_shape:
        print(
            "Max area:",
            best_area_shape,
            f"{max_area:.2f}"
        )
    if best_perimeter_shape:
        print(
            "Max perimeter:",
            best_perimeter_shape,
            f"{max_perimeter:.2f}"
        )
if __name__ == "__main__":
    file_list = [
        "input01.txt",
        "input02.txt",
        "input03.txt"
    ]
    for file_name in file_list:
        analyze_file(file_name)
