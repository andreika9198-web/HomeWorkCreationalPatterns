from __future__ import annotations
from abc import ABC, abstractmethod

class Product1:
    """Продукт — результат работы строителей. Хранит список выполненных работ."""
    def __init__(self):
        self.parts = []

class Builder(ABC):
    """Абстрактный строитель — интерфейс, который задаёт методы для всех конкретных строителей."""
    @abstractmethod
    def produce_part_a(self):
        """Первый этап работы (у каждого строителя свой)"""
        pass

    @abstractmethod
    def produce_part_b(self):
        """Второй этап работы (у каждого строителя свой)"""
        pass

class Tiler(Builder):
    """Конкретный строитель — Плиточник. Делает подготовку пола и укладку плитки."""
    def __init__(self):
        self.product = Product1()

    def produce_part_a(self):
        self.product.parts.append('Подготовка пола')

    def produce_part_b(self):
        self.product.parts.append('Укладка плитки')

class Finisher(Builder):
    """Конкретный строитель — Отделочник. Наносит шпаклёвку и штукатурит стены."""
    def __init__(self):
        self.product = Product1()

    def produce_part_a(self):
        self.product.parts.append('Нанести шпаклевку')

    def produce_part_b(self):
        self.product.parts.append('Оштукатурить стены')

class Painter(Builder):
    """Конкретный строитель — Маляр. Грунтует и красит стены."""
    def __init__(self):
        self.product = Product1()

    def produce_part_a(self):
        self.product.parts.append('Загрунтовать стену')

    def produce_part_b(self):
        self.product.parts.append('Покрасить стену')


class Foreman:
    """Директор (Прораб). Управляет строителями и знает последовательность работ."""
    def __init__(self):
        self.builder = None
        # текущий строитель
    def do_work(self, job_name):
        """Универсальный метод для любой работы"""
        print(job_name)
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        return self.builder.product.parts

    def make_paint_walls(self):
        """Покрасить стены (работа маляра)"""
        print('Красим стены:')
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        return self.builder.product.parts
    """
    Да по строителям все отлично. 
    Части a и b тут вопросов нет.
    Также понимаю логику у прораба, ты хотел конкретизировать работы.
    Но суть в том, что прораб принимает конкретного строителя и можно обойтись 1
    методом например do_work()
    """

    @staticmethod
    def make_full_renovation():
        """Работы под ключ — вызывает всех трёх строителей по очереди"""
        print('Работы под ключ:')
        total_parts = []
        for builder in [Tiler(), Finisher(), Painter()]:
            builder.produce_part_a()
            builder.produce_part_b()
            total_parts.extend(builder.product.parts)
        return total_parts

if __name__ == '__main__':
    foreman = Foreman()

    # Делаем только полы
    tiler = Tiler()
    foreman.set_builder(Tiler())
    print(foreman.do_work("Делаем полы:"))

    foreman.set_builder(Finisher())
    print(foreman.do_work("Ровняем стены:"))

    foreman.set_builder(Painter())
    print(foreman.do_work("Красим стены:"))

    # Делаем все работы под ключ
    print(foreman.make_full_renovation())



