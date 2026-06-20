class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        self._celsius = value - 273.15

    @staticmethod
    def from_fahrenheit(f):
        return Temperature((f - 32) * 5/9)

    @classmethod
    def from_kelvin(cls, k):
        return cls(k - 273.15)

    def __str__(self):
        return f"{self._celsius}"


t = Temperature(25)
print(f"25°C = {t.fahrenheit:.2f}°F = {t.kelvin:.2f}K")

t.fahrenheit = 77
print(f"После установки 77°F: {t}")

t.kelvin = 300
print(f"После установки 300K: {t}")

t2 = Temperature.from_fahrenheit(32)
print(f"32°F = {t2}")

t3 = Temperature.from_kelvin(0)
print(f"0K = {t3}")
