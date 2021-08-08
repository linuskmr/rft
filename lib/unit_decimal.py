from functools import wraps
from decimal import Decimal


class UnitDecimal(Decimal):
    """A typed Decimal, i.e. a Decimal with a unit."""

    output_decimal_points: int = 3

    unit: str
    """The unit of this Decimal."""

    def __new__(cls, value, unit: str):
        return Decimal.__new__(cls, value)

    def __init__(self, value, unit: str):
        Decimal.__init__(value)
        self.unit = unit

    def __str__(self):
        return ('{:.' + str(self.output_decimal_points) + 'f} {}').format(Decimal(self), self.unit)

    def __repr__(self):
        return str(self)


def return_unit(unit: str):
    """Changes the return type of the decorated function from Decimal to a UnitDecimal.

    :param unit: The unit of the returned UnitDecimal.
    """
    def decorator(function):
        # @wraps copies the function name, docstring and argument list from the decorated function to the wrapper.
        @wraps(function)
        def wrapper(*args, **kwargs):
            # Call function and wrap return value in UnitDecimal
            return_value = function(*args, **kwargs)
            return UnitDecimal(return_value, unit)
        return wrapper
    return decorator

