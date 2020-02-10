class Temperature:
    def __init__(self, fahrenheit=32):
        self._fahrenheit = fahrenheit
        self._celsius = self.convert_to_celsius(fahrenheit)

    def convert_to_celsius(self, f):
        return "Converted to Celsius " + str((f - 32) * (5 / 9))

    def convert_to_fahrenheit(self, c):
        return "Converted to fahrenheit: " + str((c * (9 / 5)) + 32)

    def set_fahrenheit(self, value):
        self._fahrenheit = value
        self._celsius = self.convert_to_celsius(value)
        print(self._celsius)

    def set_celsius(self, value):
        self._fahrenheit = self.convert_to_fahrenheit(value)
        self._celsius = value
        print(self._fahrenheit)

    def get_fahrenheit(self):
        return int(self._fahrenheit)

    def get_celsius(self):
        return int(self._celsius)

    fahrenheit = property(get_fahrenheit, set_fahrenheit)
    celsius = property(get_celsius, set_celsius)


t = Temperature()
t.set_fahrenheit(37)
t.set_celsius(23)
print("Given fahrenheit: ", t.get_fahrenheit())
print("Given Celsius: ", t.get_celsius())
