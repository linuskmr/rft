import math
from dataclasses import dataclass
from decimal import Decimal

from lib import konstanten
from lib.helper import grad_zu_rad
from lib.planet import ERDE
from lib.unit_decimal import UnitDecimal, return_unit


@dataclass(frozen=True)
class Bahnaufstieg:
    v_total: UnitDecimal
    """Insgesamt benötigter Schubimpuls in km/s."""


@return_unit('km/s')
def gewinn_erdrotation(beta: Decimal) -> Decimal:
    """
    Berechnet den Gewinn durch die Erdrotation auf dem Breitengrad beta.

    >>> from decimal import getcontext
    >>> getcontext().prec = 3
    >>> gewinn_erdrotation(Decimal(0))
    0.465 km/s
    >>> gewinn_erdrotation(Decimal(90))
    0.000 km/s

    Args:
        beta: Breitengrad, auf dem gestartet wird, in Grad.

    Returns:
        Decimal: Das gewonnene delta_v durch die Erdrotation.
    """
    r = ERDE.R * Decimal(math.cos(grad_zu_rad(beta)))
    return (2 * Decimal(math.pi) * r) / Decimal(konstanten.SIDERISCHER_TAG.total_seconds())


def bahnaufstieg() -> Bahnaufstieg:
    """
    Berechnet den Bahnaufstieg vom Startplaneten.

    :return: Sämtliche berechneten Werte.
    """
    # TODO: Tatsächlichen Wert ausrechnen
    print('Bahnaufstieg in eine 200-km-Bahn.')
    v_total = UnitDecimal(9.58, 'km/s')
    print(f'TODO: Fester Wert für eine 200km Umlaufbahn: {v_total=}')
    return Bahnaufstieg(v_total=v_total)