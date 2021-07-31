
class MyNumber(float):
    unit: str

    def __new__(cls, value: float, unit: str):
        return MyNumber(float.__new__(cls, value), unit)

    def __init__(self, value: float, unit: str):
        float.__init__(value)
        self.unit = unit

    def __str__(self):
        return f'{super.__str__(self)} m/s'


def str_return(function):
    def inner(*args, **kwargs):
        return_value = function(*args, **kwargs)
        return MyNumber(return_value, 'm/s')

    return inner


@str_return
def speed(distance: float, duration: float) -> float:
    return distance / duration


# print(speed(100, 10) + NumericType(3, 'm/s'))
