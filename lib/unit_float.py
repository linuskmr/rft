from functools import wraps


class UnitFloat(float):
    """A typed float, i.e. a float with a unit."""

    unit: str
    """The unit of this float."""

    def __new__(cls, value: float, unit: str):
        return float.__new__(cls, value)

    def __init__(self, value: float, unit: str):
        float.__init__(value)
        self.unit = unit

    def __str__(self):
        return f'{super.__str__(self)} {self.unit}'

    def __repr__(self):
        return f'UnitFloat({repr(float(self))}, {self.unit})'


def return_unit(unit: str):
    """Changes the return type of the decorated function from float to a UnitFloat.

    :param unit: The unit of the returned UnitFloat.
    """
    def decorator(function):
        # @wraps copies the function name, docstring and argument list from the decorated function to the wrapper.
        @wraps(function)
        def wrapper(*args, **kwargs):
            # Call function and wrap return value in UnitFloat
            return_value = function(*args, **kwargs)
            return UnitFloat(return_value, unit)
        return wrapper
    return decorator

