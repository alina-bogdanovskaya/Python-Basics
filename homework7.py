#Задача 1
from typing import List


class Matrix:
    a = []

    def __init__(self, a: List[List[float]]):
        self.a = a

    def __str__(self):
        string = ""
        for i in self.a:
            for j in i:
                string = string + " " + str(j)
            string = string + "\n"
        return string

    def __add__(self, other):
        result = []
        for i in range(len(self.a)):
            result.append([])
            for j in range(len(self.a[0])):
                result[i].append(self.a[i][j] + other.a[i][j])
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [3, 2, 1], [2, 4, 5]])
print(m1)

m2 = Matrix([[3, 6, 9], [8, 5, 2], [0, 3, 1]])
print(m2)

m3 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(m3)

print(m1 + m2 + m3)

# Задача 2
from abc import ABC, abstractmethod


class Garment(ABC):
    name = ""


    @property
    @abstractmethod
    def mat_quant(self):
        pass


class Coat(Garment):
    def __init__(self, volume):
        self.V = volume


    @property
    def mat_quant(self):
        result = self.V/6.5 + 0.5
        return result


class Suit(Garment):
    def __init__(self, height):
        self.H = height

    @property
    def mat_quant(self):
        result = 2 * self.H + 0.3
        return result


coat1 = Coat(50)
print(f'Расход ткани на пальто размера {coat1.V} составит {coat1.mat_quant:.2f}')

suit1 = Suit(1.89)
print(f'Расход ткани на костюм на рост {suit1.H} составит {suit1.mat_quant:.2f}')

print(f'Суммарный расход ткани составит {coat1.mat_quant + suit1.mat_quant:.2f}')

# Задача 3
class Cell:
    def __init__(self, cellula: int):
        self.cel = cellula

    def __add__(self, other):
        res_cell = Cell(self.cel + other.cel)
        return res_cell

    def __sub__(self, other):
        if self.cel - other.cel < 0:
            raise Exception("Unable to calculate")
        res_cell = Cell(self.cel - other.cel)
        return res_cell

    def __mul__(self, other):
        res_cell = Cell(self.cel * other.cel)
        return res_cell

    def __truediv__(self, other):
        res_cell = Cell(round(self.cel / other.cel))
        return res_cell

    def __floordiv__(self, other):
        res_cell = Cell(self.cel // other.cel)
        return res_cell

    def __str__(self):
        return str(self.cel)

    def make_order(self, cel_per_line):
        num_ful_lines = self.cel // cel_per_line
        num_last_line = self.cel % cel_per_line
        line = ('*' * cel_per_line + '\n') * num_ful_lines + '*' * num_last_line
        if num_last_line != 0:
            line = line + '\n'
        return line


cell1 = Cell(13)
cell2 = Cell(4)
cell3 = Cell(7)

print(cell1 + cell2)

try:
    print(cell1 - cell2)
except Exception as err:
    print(f'Exception: {err}')

try:
    print(cell2 - cell3)
except Exception as err:
    print(f'Exception: {err}')

print(cell2 * cell3)

print(cell2 / cell1)

print(cell3 // cell2)

print(cell2 // cell1)

print(cell1.make_order(4))

print(cell2.make_order(2))

print(cell3.make_order(3))