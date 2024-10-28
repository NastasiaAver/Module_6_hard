from math import pi, sqrt
class Figures:
    sides_count = 0
    def __init__(self, color, sides):
        self.__sides = sides
        self.__color = color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return r, g, b

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_side(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_side):
        if self.__is_valid_side(*new_side):
            self.__sides = list(new_side)

class Circle(Figures):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._Figures__sides / (2 * pi)

    def get_square(self):
        circle_square = (self.__radius ** 2) * pi
        print(circle_square)


class Triangle(Figures):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))) / self._Figure__sides[0]


    def get_square(self):
        square_tr = (self.__height * self.sides[0]) / 2
        return square_tr

class Cube(Figures):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides)


    def get_volume(self):
        cube_volume = (self._Figures__sides) ** 3
        return cube_volume


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())