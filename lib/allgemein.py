import math
from datetime import timedelta
from decimal import *
from lib.planet import Planet
from lib.unit_decimal import return_unit, UnitDecimal


def keplersche_zeitgleichung(planet: Planet, a: Decimal, epsilon: Decimal, phi: Decimal):
    return math.sqrt(a ** 3 / planet.mu) * (
            2 * math.atan(math.sqrt((1 - epsilon) / (1 + epsilon)) * math.tan(phi / 2))
            - ((float(epsilon) * math.sqrt(1 - epsilon**2) * math.sin(phi)) / (1 + float(epsilon) * math.cos(phi)))
    )


@return_unit('km')
def bahngleichung(*, p: Decimal, epsilon: Decimal, phi: Decimal) -> Decimal:
    """
    Berechnet die allgemeine Bahngleichung / Kegelschnittgleichung in Polarkoordinaten.

    :param p: Bahnparameter p.
    :param epsilon: Numerische Exzentrizität.
    :param phi: Wahre Anomalie in Radiant.
    :return: Radius r in km.
    """
    return p / (1 + epsilon * Decimal(math.cos(phi)))


@return_unit('km')
def bahngleichung_perizentrum(*, p: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet die Bahngleichung am Perizentrum, also der Ort mit minimaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Radius r in km.
    """
    return p / (1 + epsilon)


@return_unit('km')
def bahngleichung_apozentrum(*, p: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet die Bahngleichung am Apozentrum, also der Ort mit maximaler Entfernung zum Planeten.

    :param p: Bahnparameter p in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Radius r in km.
    """
    return p / (1 - epsilon)


@return_unit('km/s')
def vis_viva_r_epsilon_p(*, planet: Planet, r: Decimal, epsilon: Decimal, p: Decimal) -> Decimal:
    """
    Berechnet das Vis-Viva-Integral.

    Beispiel: Das Vis-Viva-Integral der Erde um die Sonne sollte die Geschwindigkeit der Erde ergeben.

    >>> vis_viva_r_epsilon_p(planet=SONNE, r=ERDE.a, epsilon=0, p=ERDE.a)
    29.784 km/s

    :param planet: Planet, an dem das Vis-Viva-Integral berechnet werden soll.
    :param r: Radius bzw. Abstand zum Planeten in km.
    :param epsilon: Numerische Exzentrizität der Bahn.
    :param p: Bahnparameter p in km.
    :return: Geschwindigkeit des Satelliten in km/s.
    """
    return Decimal(math.sqrt(planet.mu * ((2 / r) + ((epsilon ** 2 - 1) / p))))


@return_unit('km/s')
def vis_viva_r_a(*, planet: Planet, r: Decimal, a: Decimal) -> Decimal:
    """
    Berechnet das Vis-Viva-Integral.

    :param planet: Planet, an dem das Vis-Viva-Integral berechnet werden soll.
    :param r: Radius bzw. Abstand zum Planeten in km.
    :param a: Große Halbachse in km.
    :return: Geschwindigkeit des Satelliten in km/s.
    """
    return Decimal(math.sqrt(planet.mu * ((2 / r) - (1 / a))))


def numerische_exzentrizitaet_ra_rp(*, rp: Decimal, ra: Decimal) -> Decimal:
    """
    Berechnet die numerische Exzentrizität epsilon.

    :param ra: Radius des Apozentrums in km, also der Ort mit maximaler Entfernung zum Planten.
    :param rp: Radius des Perizentrums in km, also der Ort mit minimaler Entfernung zum Planten.
    :return: Numerische Exzentrizität.
    """
    return (ra - rp) / (ra + rp)


def numerische_exzentrizitaet_e_a(*, e: Decimal, a: Decimal) -> Decimal:
    """
    Berechnet die numerische Exzentrizität epsilon.

    :param e: Lineare Exzentrizität in km.
    :param a: Große Halbachse in km.
    :return: Numerische Exzentrizität.
    """
    return e / a


def numerische_exzentrizitaet_epsilon_a(*, epsilon: Decimal, a: Decimal) -> Decimal:
    """
    Berechnet die numerische Exzentrizität epsilon.

    :param epsilon: Numerische Exzentrizität.
    :param a: Große Halbachse in km.
    :return: Numerische Exzentrizität.
    """
    return (a * (1 + epsilon) - a * (1 - epsilon)) / (2 * a)


@return_unit('km')
def lineare_exzentrizitaet_allgemein(*, a: Decimal, epsilon: Decimal) -> Decimal:
    """
    Berechnet die lineare Exzentrizität e.

    :param a: Große Halbachse in km.
    :param epsilon: Numerische Exzentrizität.
    :return: Lineare Exzentrizität  in km.
    """
    return a * epsilon


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
