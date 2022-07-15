"""Объявите класс Track (маршрут), объекты которого создаются командой
    track = Track(start_x, start_y)
где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:
    line = TrackLine(to_x, to_y, max_speed)
где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); max_speed - максимальная скорость
на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:
    add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
    get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции сравнения:
    track1 == track2  # маршруты равны, если равны их длины
    track1 != track2  # маршруты не равны, если не равны их длины
    track1 > track2  # True, если длина пути для track1 больше, чем для track2
    track1 < track2  # True, если длина пути для track1 меньше, чем для track2

И функция:
    n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track

Создайте два маршрута track1 и track2 с координатами:
    1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
    2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90
Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq."""


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.lst = []

    def __len__(self):
        x, y = self.start_x, self.start_y
        res = 0
        for p in self.lst:
            x1, y1 = p.to_x, p.to_y
            res += ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
            x, y = x1, y1
        return int(res)

    def add_track(self, tr):
        self.lst.append(tr)

    def get_tracks(self):
        return tuple(self.lst)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

