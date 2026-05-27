from __future__ import annotations
from abc import ABC, abstractmethod


class Pasta:
    """Продукт — готовая паста. Хранит список ингредиентов."""
    def __init__(self):
        self.ingredients = []  # список ингредиентов

    def add(self, ingredient):
        """Добавить ингредиент в пасту"""
        self.ingredients.append(ingredient)

    def get_pasta(self):
        """Вернуть список всех ингредиентов"""
        return self.ingredients

class PastaBuilder(ABC):
    """Абстрактный строитель — интерфейс для создания пасты."""

    @abstractmethod
    def type_pasta(self):
        """Установить тип пасты"""
        pass

    @abstractmethod
    def add_sauce(self):
        """Добавить соус"""
        pass

    @abstractmethod
    def add_filling(self):
        """Добавить начинку"""
        pass

    @abstractmethod
    def add_topping(self):
        """Добавить добавки"""
        pass

    @abstractmethod
    def get_pasta(self):
        """Вернуть готовую пасту"""
        pass

class CarbonaraBuilder(PastaBuilder):
    """Конкретный строитель — паста Карбонара"""
    def __init__(self):
        self.pasta = Pasta()

    def type_pasta(self):
        self.pasta.add('Спагетти')

    def add_sauce(self):
        self.pasta.add('Сливочный')

    def add_filling(self):
        self.pasta.add('Бекон')

    def add_topping(self):
        self.pasta.add('Пармезан')

    def get_pasta(self):
        return self.pasta.get_pasta()

class BologneseBuilder(PastaBuilder):
    """Конкретный строитель — паста Болоньезе."""
    def __init__(self):
        self.pasta = Pasta()

    def type_pasta(self):
        self.pasta.add('Феттучини')

    def add_sauce(self):
        self.pasta.add('Томатный')

    def add_filling(self):
        self.pasta.add('Фарш')

    def add_topping(self):
        self.pasta.add('Базилик')

    def get_pasta(self):
        return self.pasta.get_pasta()

class PestoBuilder(PastaBuilder):
    """Конкретный строитель — паста Песто"""
    def __init__(self):
        self.pasta = Pasta()

    def type_pasta(self):
        self.pasta.add('Пенне')

    def add_sauce(self):
        self.pasta.add('Песто')

    def add_filling(self):
        self.pasta.add('Куриное филе')

    def add_topping(self):
        self.pasta.add('Вяленые томаты')

    def get_pasta(self):
        return self.pasta.get_pasta()


class Cook:
    """Директор (Повар). Управляет процессом приготовления пасты."""
    def __init__(self):
        self.pasta = None  # текущий строитель

    def set_pasta(self, pasta):
        """Сменить вид пасты, которую нужно приготовить"""
        self.pasta = pasta

    def make_italian_pasta_carbonara(self):
        """Приготовить Карбонару по рецепту"""
        print("Паста: Карбонара")
        self.pasta.type_pasta()
        self.pasta.add_sauce()
        self.pasta.add_filling()
        self.pasta.add_topping()
        return self.pasta.get_pasta()

    def make_italian_pasta_bolognese(self):
        """Приготовить Болоньезе по рецепту"""
        print("Паста: Болоньезе")
        self.pasta.type_pasta()
        self.pasta.add_sauce()
        self.pasta.add_filling()
        self.pasta.add_topping()
        return self.pasta.get_pasta()

    def make_italian_pasta_pesto(self):
        """Приготовить Песто по рецепту"""
        print("Паста: Песто")
        self.pasta.type_pasta()
        self.pasta.add_sauce()
        self.pasta.add_filling()
        self.pasta.add_topping()
        return self.pasta.get_pasta()

if __name__ == '__main__':
    cook = Cook()
    # Готовим Карбонару
    carbonara = CarbonaraBuilder()
    cook.set_pasta(carbonara)
    print(cook.make_italian_pasta_carbonara())
    print()

    # Готовим Болоньезе
    bolognese = BologneseBuilder()
    cook.set_pasta(bolognese)
    print(cook.make_italian_pasta_bolognese())
    print()

    # Готовим Песто
    pesto = PestoBuilder()
    cook.set_pasta(pesto)
    print(cook.make_italian_pasta_pesto())

# Паста — это сложный продукт, состоящий из нескольких частей:
# тип пасты, соус, начинка, добавки.
# Строитель позволяет собирать продукт пошагово, вызывая нужные методы
# в любом порядке.
# Директор (Повар) может управлять процессом, задавая последовательность шагов.
# В отличие от других паттернов является более гибким