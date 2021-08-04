import math
from decimal import Decimal
from lib.unit_decimal import return_unit


def raketengrundgleichung_deltav_w(*, delta_v: Decimal, w: Decimal) -> Decimal:
    """
    Die Raketengrundgleichung.

    >>> from decimal import getcontext
    >>> getcontext().prec = 4
    >>> raketengrundgleichung_deltav_w(delta_v=Decimal('9.7'), w=Decimal('3'))
    0.039

    Args:
        delta_v: Geschwindigkeitszuwachs in km/s.
        w: Effektive Ausströmgeschwindigkeit der Gase in km/s.

    Returns:
        Das Verhältnis mb/m0.
    """
    return (-(delta_v / w)).exp()


@return_unit('km/s')
def geschwindigkeitszuwachs_raketengrundgleichung(*, w: Decimal, mb: Decimal, m0: Decimal) -> Decimal:
    """
    Raketengrundgleichung, die den Geschwindigkeitszuwachs berechnet.

    Args:
        w: Effektive Ausströmgeschwindigkeit in km/s.
        mb: Brennschlussmasse in kg (Konstruktionsmasse + Nutzlast).
        m0: Startmasse in kg (Masse Rakete + Treibstoff + Nutzlast).

    Returns:
        Decimal: Delta v bzw. Geschwindigkeitszuwachs in km/s.
    """
    return -w * Decimal(math.log(mb / m0))


@return_unit('km/s')
def schub_m_m(*, w: Decimal, m_punkt: Decimal) -> Decimal:
    """
    Berechnet den Schub einer Rakete.

    Args:
        w: Strahlaustrittsgeschwindigkeit w in km/s.
        m_punkt: Massenstrom in kg/s.

    Returns:
        Decimal: Schub F in km/s.
    """
    return w * m_punkt
