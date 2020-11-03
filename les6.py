import datetime as dt


class Robot(object):
    def __init__(self, os):
        self.os = os

    def run(self):
        print(f'{self.os} loading')


class Car:
    _collection = []
    __secret = 'HELLO SECRET'

    def __init__(self, engine, brand, create_age):
        """"""
        self.engine = engine
        self.brand = brand
        self.create_age = create_age
        self._collection.append(self)

    def run(self):
        print(f'Start {self.engine} engine')
        for _ in range(3):
            print('Дыр')
        self.hong()

    def hong(self):
        print('БИП')

    def get_secret(self):
        return self.__secret


class FordPickUp(Car):
    _collection = []

    def __init__(self, name, carrying):
        self.name = name
        self.carrying = carrying
        super().__init__(6.3, 'FORD', dt.datetime.now().year)

    def hong(self):
        print('AAAAAAAAAAAAAAAAA')
        super().hong()


class Transformer(FordPickUp, Robot):
    def __init__(self, name):
        super().__init__(name, 10000)
        Robot.__init__(self, 'SparkOS')


ford_t = Car(1.8, 'Ford', 1932)
chevrolet = Car(6, 'chevrolet', 1987)

p_ford = FordPickUp('Raptor', 2000)
transformer = Transformer('Optimus')
