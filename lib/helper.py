from lib.unit_decimal import return_unit
from decimal import Decimal
import math
from datetime import datetime


@return_unit("°")
def rad_zu_grad(rad: Decimal) -> Decimal:
    """Konvertiert Wert von Radiant/Bogenmaß zu Grad.

    >>> import lib.unit_decimal
    >>> lib.unit_decimal.UnitDecimal.output_decimal_points = 3
    >>> rad_zu_grad(rad=Decimal(0))
    0.000 °
    >>> rad_zu_grad(rad=Decimal(math.pi))
    180.000 °

    Args:
        rad (Decimal): Ursprungswert in Radiant.

    Returns:
        Decimal: Gleicher Wert in Grad.
    """
    return rad / Decimal(math.pi) * 180


@return_unit("rad")
def grad_zu_rad(grad: Decimal) -> Decimal:
    """Konvertiert Wert von Grad zu Radiant/Bogenmaß.

    >>> import lib.unit_decimal
    >>> lib.unit_decimal.UnitDecimal.output_decimal_points = 3
    >>> grad_zu_rad(grad=0)
    0.000 rad
    >>> grad_zu_rad(grad=180)
    3.142 rad

    Args:
        grad (Decimal): Ursprungswert in Grad.

    Returns:
        Decimal: Gleicher Wert in Rad.
    """
    return grad * Decimal(math.pi) / 180


def gleicher_tag(datum1: datetime, datum2: datetime) -> bool:
    """Vergleicht zwei Daten unabhängig von der Zeit.

    Args:
        datum1 (datetime): Erstes Datum.
        datum2 (datetime): Zweites Datum.

    Returns:
        bool: True, wenn Jahr, Monat und Tag übereinstimmen.
    """
    return datum1.year == datum2.year and datum1.month == datum2.month and datum1.day == datum2.day
