
class UnitFloat(float):
    unit: str

    def __new__(cls, value: float, unit: str):
        return float.__new__(cls, value)

    def __init__(self, value: float, unit: str):
        float.__init__(value)
        self.unit = unit

    def __str__(self):
        return f'{super.__str__(self)} {self.unit}'


def return_unit(unit: str):
    def decorator(function):
        def wrapper(*args, **kwargs):
            return_value = function(*args, **kwargs)
            return UnitFloat(return_value, unit)
        return wrapper
    return decorator

