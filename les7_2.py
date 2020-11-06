class Temperature:
    __KELVIN_CONST_C = 273.15
    __slots__ = ('kelvin',)

    def __init__(self):
        self.kelvin = 0

    @property
    def celsius(self):
        return self.kelvin - self.__KELVIN_CONST_C

    @celsius.setter
    def celsius(self, value):
        self.kelvin = value + self.__KELVIN_CONST_C

    @property
    def fahrenheit(self):
        return self.kelvin * 1.8 - 459.67

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.kelvin = (value + 459.67) / 1.8


if __name__ == '__main__':
    termo = Temperature()
    termo.kelvin = 300
    print(termo.celsius)
    termo.fahrenheit = 120
    print(termo.kelvin)
    print(termo.celsius)
    print(1)
