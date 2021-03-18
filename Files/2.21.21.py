class Temperature:

    def __init__(self, celsius=None, fahrenheit=None, kelvin=None):
        self._celsius = celsius
        self._fahrenheit = fahrenheit
        self._kelvin = kelvin

    @property
    def celsius(self):
        if self._celsius is not None:
            return self._celsius
        elif self._fahrenheit is not None:
            return (self._fahrenheit - 32) * 5/9
        else:
            return self._kelvin - 273.15

    @property
    def kelvin(self):
        if self._kelvin is not None:
            return self._kelvin
        elif self._celsius is not None:
            return self._celsius + 273.15

    @property
    def fahrenheit(self):
        if self._fahrenheit is not None:
            return self._fahrenheit
        elif self._celsius is not None:
            return (self._celsius * 9/5) + 32
        else:
            return (1°F – 32) x 5/9 + 273.15



# temp_1 = Temperature(celsius=30.0)
#  temp_2 = Temperature(fahrenheit=98.6)
#  temp_3 = Temperature(kelvin=310.15)

assert Temperature(celsius=30.0).kelvin == 303.15
assert Temperature(celsius=40.0).fahrenheit == 104

assert Temperature(fahrenheit=98.6).celsius == 30.0
assert Temperature(fahrenheit=98.6).celsius == 371.75