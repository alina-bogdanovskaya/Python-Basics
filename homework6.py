# Задача 1
import time


class TrafficLight:
    __color = -1
    list_color = [{"color": "red", "time": 7}, {"color": "yellow", "time": 2}, {"color": "green", "time": 15}]

    def running(self):
        self.__color += 1
        if self.__color > 2:
            self.__color = 0
        state = self.list_color[self.__color]
        print(state["color"])
        time.sleep(state["time"])


crossroad_1 = TrafficLight()
for i in range(6):
    crossroad_1.running()


# Задача 2
a_mass_per_m = 25
thick = input("Please enter desired thickness of covering in cm:")


class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width
        print(self._l, self._w)

    def tarmac(self):
        asphalt = float(self._l) * float(self._w) * a_mass_per_m * float(thick)
        return asphalt


r1 = Road(22000, 100)
r1.tarmac()
print(r1.tarmac()/1000)


# Задача 3
class Worker:
    def __init__(self, name, surname, position, x, y):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": x, "bonus": y}
        return


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


p1 = Position("Peter", "Crowd", "Senior CRA", 30000, 3600)
print(p1.get_full_name())
print(p1.get_total_income())
print(p1.position)

p2 = Position("Mary", "Brown", "Clinical Lead", 50000, 25000)
print(p2.get_full_name())
print(p2.get_total_income())
print(p2.position)


# Задача 4
class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car pulled away")

    def stop(self):
        print("Car stopped")

    def turn(self, direction):
        print(f"Car turned {direction}")

    def show_speed(self):
        print(f"Car speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.is_police is False and self.speed > 60:
            print(f"Car speed is {self.speed}. Over speed limit")
        else:
            print(f"Car speed is {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Car speed is {self.speed}. Over speed limit")
        else:
            print(f"Car speed is {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


def car_info(my_car):
    if isinstance(my_car, PoliceCar) is True:
        print(f"This is a police {my_car.color} {my_car.name}")
    elif my_car.is_police is True:
        print(f"This is a civil {my_car.color} {my_car.name} used by police")
    else:
        print(f"This is a civil {my_car.color} {my_car.name}")


police1 = PoliceCar(90, "blue", "Lexus")
car_info(police1)
police1.show_speed()

work1 = WorkCar(55, "white", "SUV", False)
car_info(work1)
work1.show_speed()

town1 = TownCar(55, "red", "VW", False)
car_info(town1)
town1.show_speed()

town2 = TownCar(75, "orange sunset", "Kia", False)
car_info(town2)
town2.show_speed()

town3 = TownCar(99, "silver", "Audi", True)
car_info(town3)
town3.show_speed()

sport1 = SportCar(120, "yellow", "Lamborghini", False)
car_info(sport1)
sport1.show_speed()


# Задача 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


red_pen = Pen("красная ручка")
red_pen.draw()

green_pencil = Pencil("зеленый карандаш")
green_pencil.draw()

purple_handle = Handle("лиловый маркер")
purple_handle.draw()
